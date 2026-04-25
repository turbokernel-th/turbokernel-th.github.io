---
title: "Hotel Pricing & Inventory Model"
date: 2025-02-01
draft: false
summary: "โมเดล Predictive ประสิทธิภาพสูงสำหรับการตั้งราคาและจัดการ Inventory ของโรงแรม ที่มีความแม่นยำถึง 85%"
tags: ["Data Science", "Predictive Modeling", "Hospitality", "Python"]
---

## ภาพรวมของโปรเจกต์

ช่วงที่ผมทำงานอยู่ที่ **Datawealth** ผมได้พัฒนา Predictive models เพื่อปรับปรุงกลยุทธ์การตั้งราคา (Pricing) และการจัดการ Inventory ของโรงแรมให้มีประสิทธิภาพสูงสุด

## ผลลัพธ์สำคัญ

- **Pricing Model:** ทำความแม่นยำได้ถึง **85% (15% MAPE)** โมเดลนี้จะวิเคราะห์ข้อมูลประวัติการจอง, ฤดูกาล (Seasonality), และราคาของคู่แข่ง เพื่อแนะนำราคาห้องพักที่เหมาะสมที่สุด
- **Inventory Management:** โมเดล Proof of Concept (PoC) ทำความแม่นยำได้ถึง **94%** ช่วยคาดการณ์ Demand ของห้องพัก และป้องกันปัญหาการรับจองเกิน (Overbooking) หรือห้องว่างเกินความจำเป็น (Under-utilization)
- **Impact:** เครื่องมือเหล่านี้ช่วยให้สามารถวางกลยุทธ์การตั้งราคาที่ส่งผลโดยตรงต่อการเติบโตของรายได้และการลดต้นทุนของธุรกิจ

## Dashboards & Analytics
นอกจากการทำโมเดลแล้ว ผมยังได้สร้าง Self-service analytics dashboards ซึ่งช่วยให้ทีมที่ไม่ได้มีพื้นฐานทางเทคนิค (Non-technical stakeholders) สามารถดึงรีพอร์ตและมอนิเตอร์ประสิทธิภาพการดำเนินงานของแต่ละหน่วยธุรกิจได้ด้วยตัวเอง

## เทคโนโลยีที่ใช้
- **Python (Pandas, Scikit-learn)**
- **SQL** สำหรับดึงข้อมูล
- **Visualization Tools** สำหรับทำ Dashboards
