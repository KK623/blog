const { createCanvas } = require('canvas');
const fs = require('fs');

const canvas = createCanvas(800, 900);
const ctx = canvas.getContext('2d');

// Background
ctx.fillStyle = '#f8f9fa';
ctx.fillRect(0, 0, 800, 900);

// Title
ctx.fillStyle = '#2c3e50';
ctx.font = 'bold 36px sans-serif';
ctx.textAlign = 'center';
ctx.fillText('婴儿车推荐指南', 400, 60);

ctx.font = '20px sans-serif';
ctx.fillStyle = '#7f8c8d';
ctx.fillText('预算 2000-5000 | 适用 0-4岁', 400, 95);

// Line
ctx.strokeStyle = '#3498db';
ctx.lineWidth = 2;
ctx.beginPath();
ctx.moveTo(50, 115);
ctx.lineTo(750, 115);
ctx.stroke();

// Data
const products = [
  { name: 'UPPAbaby Cruz V2', price: '~5000', feature: '品质+保值首选', color: '#27ae60' },
  { name: 'Bugaboo Butterfly', price: '~4500', feature: '轻便+避震好', color: '#9b59b6' },
  { name: 'Bugaboo Cameleon 3 Plus', price: '~5500', feature: '经典款耐用', color: '#e67e22' },
  { name: 'YOYO3', price: '~4500', feature: '最轻便、登机神器', color: '#3498db' },
  { name: 'Stokke Xplory X', price: '~7000+', feature: '颜值天花板', color: '#e74c3c' },
  { name: 'Bugaboo Fox2', price: '~7000+', feature: '舒适度天花板', color: '#1abc9c' },
];

let y = 150;
products.forEach((p, i) => {
  // Card background
  ctx.fillStyle = '#ffffff';
  ctx.shadowColor = 'rgba(0,0,0,0.1)';
  ctx.shadowBlur = 10;
  ctx.fillRect(50, y, 700, 100);
  ctx.shadowBlur = 0;
  
  // Number
  ctx.fillStyle = p.color;
  ctx.font = 'bold 28px sans-serif';
  ctx.textAlign = 'left';
  ctx.fillText(`${i + 1}`, 70, y + 45);
  
  // Name
  ctx.fillStyle = '#2c3e50';
  ctx.font = 'bold 22px sans-serif';
  ctx.fillText(p.name, 120, y + 35);
  
  // Price
  ctx.fillStyle = p.color;
  ctx.font = 'bold 20px sans-serif';
  ctx.textAlign = 'right';
  ctx.fillText(p.price, 720, y + 35);
  
  // Feature
  ctx.fillStyle = '#7f8c8d';
  ctx.font = '18px sans-serif';
  ctx.textAlign = 'left';
  ctx.fillText(p.feature, 120, y + 70);
  
  y += 115;
});

// Recommendation box
y += 20;
ctx.fillStyle = '#27ae60';
ctx.fillRect(50, y, 700, 80);
ctx.fillStyle = '#ffffff';
ctx.font = 'bold 22px sans-serif';
ctx.textAlign = 'center';
ctx.fillText('首选推荐: UPPAbaby Cruz V2 或 Bugaboo Butterfly', 400, y + 48);

// Footer
ctx.fillStyle = '#7f8c8d';
ctx.font = '16px sans-serif';
ctx.fillText('数据仅供参考，请以实际价格为准', 400, 870);

// Save
const buffer = canvas.toBuffer('image/png');
fs.writeFileSync('/root/.openclaw/workspace/baby-stroller.png', buffer);
console.log('Image saved!');
