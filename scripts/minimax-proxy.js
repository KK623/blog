const http = require('http');
const https = require('https');

const MINIMAX_API_KEY = "sk-api-f6jf64dckV7ptPIjYsgVfU6peViDV_pbttmeQkPX9_qfb-sQr8LSzF4d-KsD3yur6BNi83MJrSayboALm6ofDG3qpK5E38XUyoiECvHKfAILY9EweSlyXUE";
const MINIMAX_BASE_URL = "api.minimax.chat";
const PORT = 8081;

function makeRequest(options, body) {
  return new Promise((resolve, reject) => {
    const req = https.request(options, (res) => {
      let data = "";
      res.on("data", chunk => data += chunk);
      res.on("end", () => resolve({ status: res.statusCode, body: data }));
    });
    req.on("error", reject);
    if (body) req.write(body);
    req.end();
  });
}

const server = http.createServer(async (req, res) => {
  console.log(`Received: ${req.method} ${req.url}`);
  
  if (req.url === "/v1/messages" && req.method === "POST") {
    let body = "";
    req.on("data", chunk => body += chunk);
    req.on("end", async () => {
      try {
        const msg = JSON.parse(body);
        
        // Convert Anthropic format to MiniMax format
        const messages = msg.messages.map(m => {
          if (typeof m.content === 'string') {
            return { role: m.role === "assistant" ? "assistant" : "user", content: m.content };
          }
          // Handle content blocks
          if (Array.isArray(m.content)) {
            const text = m.content.find(c => c.type === 'text')?.text || '';
            return { role: m.role === "assistant" ? "assistant" : "user", content: text };
          }
          return { role: m.role, content: String(m.content) };
        });
        
        const mmBody = JSON.stringify({
          model: "MiniMax-M2",
          messages: messages,
          max_tokens: msg.max_tokens || 1024
        });
        
        console.log("Sending to MiniMax:", mmBody.substring(0, 100));
        
        const response = await makeRequest({
          hostname: MINIMAX_BASE_URL,
          path: "/v1/text/chatcompletion_v2",
          method: "POST",
          headers: {
            "Authorization": `Bearer ${MINIMAX_API_KEY}`,
            "Content-Type": "application/json"
          }
        }, mmBody);
        
        console.log("MiniMax response:", response.status, response.body.substring(0, 100));
        
        // Convert MiniMax response back to Anthropic format
        const mmResp = JSON.parse(response.body);
        const content = mmResp.choices?.[0]?.message?.content || "";
        
        const anthropicResp = {
          id: mmResp.id || `msg_${Date.now()}`,
          type: "message",
          role: "assistant",
          content: content,
          model: mmResp.model || "MiniMax-M2",
          stop_reason: mmResp.choices?.[0]?.finish_reason || "end_turn",
          stop_sequence: null,
          usage: {
            input_tokens: mmResp.usage?.prompt_tokens || 0,
            output_tokens: mmResp.usage?.completion_tokens || 0
          }
        };
        
        res.writeHead(200, { 
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        });
        res.end(JSON.stringify(anthropicResp));
      } catch (e) {
        console.error("Error:", e.message);
        res.writeHead(500, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: { type: "server_error", message: e.message } }));
      }
    });
  } else if (req.method === 'OPTIONS') {
    res.writeHead(204, {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, Authorization"
    });
    res.end();
  } else {
    res.writeHead(404);
    res.end();
  }
});

server.listen(PORT, () => {
  console.log(`Proxy running on http://localhost:${PORT}`);
});
