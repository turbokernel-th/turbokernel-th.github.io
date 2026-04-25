---
title: "Saifa Application - Agentic AI Workflows"
date: 2025-11-01
draft: false
summary: "เพิ่มความเร็วในการ Inference ขึ้น 30% และปรับแต่งประสิทธิภาพระบบ RAG สำหรับแอปพลิเคชัน AI Agent"
tags: ["AI", "RAG", "Optimization", "Python"]
---

## ภาพรวมของโปรเจกต์

ที่ **Saifa AI Inc.** ผมได้ร่วมพัฒนา Core AI engine สำหรับแอปพลิเคชัน Saifa โดยมีเป้าหมายเพื่อเพิ่มความรวดเร็วในการตอบสนองและความแม่นยำของ AI agents

## ผลงานสำคัญ

### Agentic AI Workflows
ผมได้ออกแบบ Workflows ใหม่ที่ช่วยให้กระบวนการตัดสินใจของ AI agents เป็นระบบและลื่นไหลมากขึ้น
- **Result:** เพิ่มความเร็วในการทำ Inference ได้ถึง **30%**
- **Feature:** พัฒนาระบบเรนเดอร์ "Thinking process" ที่ช่วยให้ผู้ใช้เห็นลอจิกการทำงานของ Agent ได้แบบเรียลไทม์ ซึ่งช่วยสร้างความน่าเชื่อถือและพัฒนา User experience ให้ดีขึ้น

### RAG System Optimization
ระบบ Retrieval-Augmented Generation (RAG) เดิมมีปัญหาท้าทายเรื่องความแม่นยำ (Precision)
- **Action:** ผมปรับปรุง Architecture ใหม่ โดยเน้นไปที่กลยุทธ์การทำ Chunking ที่ดีขึ้นและการทำ Retrieval ranking
- **Result:** เพิ่ม **precision@5 จาก 76% เป็น 90%** หรือคิดเป็นการพัฒนาคุณภาพของ Retrieval ถึง 14%

## เทคโนโลยีที่ใช้
- **LangGraph** สำหรับ Agent workflows
- **QDrant** สำหรับ Vector storage
- **Python/FastAPI** สำหรับ Backend services
