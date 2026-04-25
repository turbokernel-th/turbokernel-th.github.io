---
title: "Coding Agent สำหรับทุกคน — บทนำ: สมมติว่าเราเขียนโค้ดด้วยภาษาไทย แล้วมัน work?"
date: 2026-04-25
draft: false
post_type: "Blog Post"
tags: ["Introduction", "AI", "Coding Agent", "OpenCode", "Claude Code", "Gemini", "Productivity", "Fun", "Python", "Gradio"]
summary: "คุณไม่จำเป็นต้องเป็นวิศวกรก็ใช้ Coding Agent ได้ บทนำนี้จะแสดงให้เห็นว่าเราทำอะไรได้บ้าง ตั้งแต่ app แต่งรูป slide presentation 8 หน้า ไปจนถึง dashboard ข้อมูลแบบสดๆ ทั้งหมดนี้สร้างได้แค่เพียง 'เอ่ยปากถาม'"
---

ช่วงนี้ผมสนุกกับการใช้ [Coding Agent](https://github.com/google-gemini/gemini-cli) มากครับ ลองนึกภาพว่ามันคือ "ผู้ช่วยส่วนตัว" (อารมณ์เหมือนมี Jarvis ประจำตัว) แทนที่จะแค่ตอบคำถามเหมือน [chatbot](https://chatgpt.com) ทั่วไป เจ้าเอเจนท์ตัวนี้จะรับคำสั่งแล้วลงมือทำตามขั้นตอนต่าง ๆ ให้เราจนเสร็จงาน เพียงแค่เราบอกความต้องการ มันทำงานผ่าน `terminal` สามารถอ่านไฟล์ เขียนโค้ด และแก้ `bug` ได้เองจนจบงาน

บทความนี้เหมาะสำหรับทุกคนที่อยากสร้างอะไรบางอย่างแต่ติดที่เขียนโค้ดไม่เป็น ไม่ว่าจะเป็นการทำกราฟสวยๆ สรุปไฟล์ `PDF` กองโต หรือสั่งให้คอมทำงานน่าเบื่อแทน การมีเอเจนท์ช่วยจัดการเรื่อง "how-to" ทำให้เราโฟกัสที่ "จินตนาการ" ได้เต็มที่ครับ

การเริ่มต้นก็ไม่แพงอย่างที่คิด มีตัวเลือก [open-source](https://opensource.org/) อย่าง [OpenCode](https://opencode.ai) ที่ใช้คู่กับ [Gemini](https://gemini.google.com) ตัวฟรีได้ หรือถ้าอยากได้ความล้ำขึ้นไปอีกก็ขยับไปใช้ [Claude Code](https://claude.ai/code) ได้ `series` นี้จะพาไปดูทั้งสองทาง โดยตัวอย่างด้านล่างนี้ผมใช้ [Gemini CLI](https://github.com/google-gemini/gemini-cli) สร้างขึ้นมาฟรีทั้งหมดครับ

## ตัวอย่างสิ่งที่ทำได้

1. **สร้างเครื่องมือใหม่จากศูนย์**: ผมลองสั่งให้ทำโปรแกรมแต่งรูป
   - เอเจนท์เลือกใช้ `library` อย่าง [`gradio`](https://www.gradio.app/) และ [`pillow`](https://python-pillow.org/) เอง
   - ติดตั้งและเขียนโค้ดสร้าง `web app` ให้เสร็จสรรพ พร้อมเพิ่ม `feature` ปรับความสว่าง และใส่ `filter` สวยๆ ให้โดยที่ผมไม่ได้เขียนโค้ดสักบรรัด
   {{< gdrive id="1c2j2QGwdd9nTNAx5pVncbVRNs302_cUz" >}}

2. **สรุปข้อมูลปริมาณมาก**: ผมส่งรายงานเศรษฐกิจยาวๆ เป็น `PDF` ให้มันทำเป็น `presentation`
   - เอเจนท์อ่านเอกสารและดึงประเด็นสำคัญ เช่น `GDP` หรือราคาน้ำมันมาสรุป
   - ออกแบบ `slide` ให้ 8 หน้า พร้อมสร้างไฟล์ [`PowerPoint`](https://www.microsoft.com/en-us/microsoft-365/powerpoint) และ `PDF` ให้ทันที ช่วยประหยัดเวลาได้มหาศาล
   {{< gdrive id="1rBa8NJbeSvrHI_qD0uiMQOcnG0OV2_Xt" >}}

3. **จัดการข้อมูลที่ยุ่งเหยิง**: ผมส่งโฟลเดอร์ข้อมูลดิบให้เอเจนท์
   - ใช้ `library` [`pandas`](https://pandas.pydata.org/) ทำความสะอาดข้อมูล
   - สร้าง `dashboard` แบบโต้ตอบได้และ `slide presentation` ที่ข้อมูลตรงกันเป๊ะ เหมือนมีนักวิเคราะห์ข้อมูลมาทำให้เลย
   {{< gdrive id="1RSV1plXwxuLvmv_x6uSMV293ryk1Z9tI" >}}

## แผนการเดินทางของเรา

| # | หัวข้อ | รายละเอียด |
|---|---|---|
| **0** | **บทนำ** *(คุณอยู่ตรงนี้)* | ภาพรวมและตัวอย่างสิ่งที่ทำได้ |
| **1** | **พื้นฐานที่ควรรู้** | เรื่องของ `terminal`, `Python` และการทำงานของเอเจนท์ |
| **2** | **ติดตั้งเอเจนท์ตัวแรก** | เริ่มต้นใช้งาน `OpenCode` และ `Claude Code` จากศูนย์ |
| **3** | **ปรับแต่งให้เข้ามือ** | วิธีใช้ `custom prompt` และเพิ่มทักษะใหม่ๆ |
| **4** | **แบ่งปันผลงาน** | วิธีนำสิ่งที่สร้างขึ้นไป `online` ให้คนอื่นใช้ |

ตอนต่อไปจะเริ่มเข้าสู่เนื้อหาเทคนิคเล็กน้อยครับ การรู้พื้นฐานว่า `terminal` ทำงานยังไง หรือ `AI` ตัดสินใจแบบไหน จะช่วยให้เราสร้างสิ่งที่ซับซ้อนขึ้นได้มาก พอพื้นฐานแม่นแล้วความสนุกจะเริ่มขึ้นครับ

## ลิงก์ที่น่าสนใจ

**Coding Agent:**
- [Claude Code](https://claude.ai/code) — ตัวท็อปจาก Anthropic (มีค่าใช้จ่าย)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) — `open-source` จาก Google
- [OpenCode](https://opencode.ai) — ทำงานร่วมกับ `Gemini` ได้ดีมาก

**Terminal:**
- [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell) — สำหรับ Windows
- [Terminal / Bash](https://support.apple.com/guide/terminal/welcome/mac) — สำหรับ macOS และ Linux

**Language & Runtime:**
- [Python](https://www.python.org/downloads/) — ภาษาหลักที่ใช้ใน `project`
- [Node.js](https://nodejs.org/) — สำหรับ `Gemini CLI` และ `JavaScript`
