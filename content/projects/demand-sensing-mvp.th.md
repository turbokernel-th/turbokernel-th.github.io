---
title: "Real-time Demand Sensing MVP"
date: 2024-01-01
draft: false
summary: "MVP ผลงานรางวัลชนะเลิศที่ผสานข้อมูลเศรษฐกิจและสภาพอากาศเพื่อคาดการณ์ความผันผวนของ Demand ในตลาด"
tags: ["XGBoost", "Competition", "Data Engineering"]
---

## ภาพรวมของโปรเจกต์

โปรเจกต์นี้ถูกพัฒนาขึ้นสำหรับการแข่งขัน **E-SAN PMU-B Coding & AI Competition** ซึ่งทีมของผม ("Team Orange Cat") ได้รับรางวัลชนะเลิศใน **Data Science Track**

## โซลูชันของเรา
เราได้สร้าง Minimum Viable Product (MVP) สำหรับทำ Real-time Demand Sensing เพื่อช่วยให้ธุรกิจสามารถคาดการณ์ความผันผวนของตลาดได้ล่วงหน้า

### วิธีการทำงาน
- **Data Integration:** เราใช้ Python เขียน web crawlers และต่อ API เพื่อดึง Open Data ที่หลากหลายมาใช้ เช่น:
    - รูปแบบสภาพอากาศ (Weather patterns)
    - การเปลี่ยนแปลงทางประชากรศาสตร์
    - ตัวชี้วัดทางเศรษฐกิจ
- **Modeling:** เราเทรนโมเดล **XGBoost** เพื่อวิเคราะห์ปัจจัยภายนอกเหล่านี้ ร่วมกับข้อมูลยอดขายภายในของธุรกิจ

## ผลลัพธ์
เครื่องมือนี้ช่วยให้ Insights ที่สามารถนำไปใช้งานได้จริงในการวางแผนกลยุทธ์ ทำให้ธุรกิจสามารถปรับตัวเรื่อง Supply Chain และจัดการ Inventory ได้ตอบรับกับสัญญาณที่เกิดขึ้นแบบเรียลไทม์

## เทคโนโลยีที่ใช้
- **XGBoost**
- **Python** (Web Scraping, APIs)
- **Data Engineering Pipelines**
