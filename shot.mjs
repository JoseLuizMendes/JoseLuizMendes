import pw from '/home/claude/.npm-global/lib/node_modules/playwright/index.js';
const { chromium } = pw;
const jobs = JSON.parse(process.argv[2]);
const b = await chromium.launch();
for (const j of jobs) {
  const p = await b.newPage({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: 2 });
  await p.goto('file://' + process.cwd() + '/' + j.html);
  await p.waitForTimeout(700);
  await p.screenshot({ path: j.out });
  console.log('wrote', j.out);
  await p.close();
}
await b.close();
