# 星米医疗官网设计方案

> 保存日期：2026-05-30
> 状态：在线 → https://ef6d0e6ce87242f1b53f1885cc34cbe8.app.codebuddy.work

---

## 一、站点架构

### 单页应用（SPA）+ 独立详情页
```
index.html          ← 主站（单页，含全部 section）
├── #hero           ← 首屏
├── #products       ← 产品中心（Tab切换）
├── #videos         ← 产品视频
├── #news           ← 新闻动态（展开/收起）
├── #careers        ← 人才招聘
├── #faq            ← 常见问题
├── #manuals        ← 使用说明书
├── #contact        ← 联系我们
└── footer

news-detail.html    ← 新闻详情（id参数路由）
images/logo.png     ← 品牌Logo
```

### 新闻详情架构
```javascript
// URL参数: news-detail.html?id=20260525
var newsData = {
  "20260525": { title, date, body: `...` },
  "202511": { ... },
  // ... 共18篇
};
```

---

## 二、设计系统

### 色彩体系

| Token | 值 | 用途 |
|-------|-----|------|
| `--blue` | `#00B4D8` | 主色：按钮、链接、强调 |
| `--blue-deep` | `#023E8A` | 深蓝：标题、渐变终点 |
| `--blue-light` | `#48CAE4` | 浅蓝：渐变、辅助 |
| `--accent` | `#FF6B35` | 橙色：热点、新品标记 |
| `--green` | `#06D6A0` | 绿色：认证、成功、完成 |
| `--gray-50` | `#F8FAFC` | 背景浅灰 |
| `--gray-100` | `#F1F5F9` | 分隔、卡片悬停 |
| `--gray-200` | `#E2E8F0` | 边框、分割线 |
| `--gray-400` | `#94A3B8` | 次要文字 |
| `--gray-600` | `#64748B` | 正文 |
| `--gray-800` | `#1E293B` | 标题、主文字 |

### 渐变组合
- **Hero 背景**: `#FFF7ED → #E0F4FE → #F0FDF4 → #FFF`
- **主按钮**: `#00B4D8 → #48CAE4`
- **标题渐变**: `#00B4D8 → #023E8A`
- **R&D 背景**: `#023E8A → #014B8A → #00B4D8`
- **Footer**: `#0A2540`

### 排版
| 层级 | 字号 | 字重 | 用途 |
|-----|------|------|------|
| H1 | 48px | 900 | Hero 标题 |
| H2 | 36px | 800 | Section 标题 |
| H3 | 20-28px | 700-800 | 卡片标题、统计数字 |
| H4 | 14-16px | 600-700 | 新闻标题、卡片副标题 |
| Body | 14-18px | 400 | 正文 |
| Small | 12-13px | 400-600 | 日期、标签、辅助信息 |
| Label | 13px | 700 | Section 标签（大写+letter-spacing） |

字体栈：`-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif`

### 间距
- Section padding: `90px 0`
- Container: `max-width: 1200px, padding: 0 24px`
- 卡片间距: `24-28px`（grid gap）
- 内边距: 18-36px（根据卡片类型）

---

## 三、布局系统

### 网格
| 区域 | 桌面 | 平板(≤900px) | 手机(≤560px) |
|-----|------|-------------|-------------|
| Hero | `flex` 左右 | `flex` 上下 | 同平板 |
| 产品型号 | 3列 grid | 2列 | 1列 |
| 产品视频 | 3列 grid | 2列 | 1列 |
| 核心优势 | 3列 grid | 1列 | 1列 |
| 研发中心 | 2列 grid | 1列 | 1列 |
| 新闻动态 | 2:1 grid | 1列 | 1列 |
| 人才福利 | 2列 grid | 1列 | 1列 |
| 人才岗位 | 2列 grid | 1列 | 1列 |
| 培养计划 | 4列 grid | 2列 | 1列 |
| 联系我们 | 2列 grid | 1列 | 1列 |
| Footer | 2:1:1:1 grid | 2列 | 1列 |

---

## 四、组件目录

### 1. 导航栏 `.navbar`
- 固定置顶，毛玻璃效果（backdrop-filter: blur(16px)）
- Logo + 6个链接 + CTA按钮
- 滚动后加阴影（`.scrolled`）
- 移动端汉堡菜单

### 2. Hero `.hero`
- 渐变背景 + 径向光晕装饰
- 左侧文字 + 右侧轮播图（3图自动播放+手动切换）
- 统计数字行：6证 | 19专利 | 7大产品线

### 3. 产品中心 `#products`
- Tab 切换：制氧机 / 雾化器 / 吸痰器 / 肺功能训练仪 / 洗鼻器
- `.cat-tab` 药丸型标签，激活态蓝色填充
- `.cat-panel` 面板，`display:none/block` 切换
- `.models-grid` 3列型号卡片
- `.model-card`: 产品图(220px) + 规格表(2列grid) + 标签徽章

### 4. 产品视频 `#videos`
- Tab 切换（制氧机/雾化器），同类内部还有子分组
- `.video-card`: 缩略图(220px) + 播放按钮 + 时长 + 标题
- 视频弹窗 `.video-modal`：全屏85%黑底，居中播放

### 5. 核心优势 `.advantage-grid`
- 3列 `.adv-card`，圆形图标 + 标题 + 描述
- Hover 上浮 + 蓝色背景

### 6. 研发中心 `.rd-section`
- 深蓝渐变背景，白色文字
- 2列 `.rd-card`：毛玻璃半透明卡片
- 深圳（前端创新）+ 泰州（工艺制造）

### 7. 新闻动态 `#news`（当前18篇）
- 布局：左侧 **主推新闻**（大卡片 280px图 + 正文）+ 右侧 **新闻列表**
- 新闻列表：**默认展示前6篇**，其余折叠 → 底部 "展开全部（共18篇）" 按钮
- `.news-item`: 水平排列（SVG缩略图64×64 + 日期 + 标题 + 摘要）
- 展开/收起JS逻辑：
  ```javascript
  function toggleNews() {
    var el = document.getElementById('news-hidden');
    var btn = document.getElementById('newsExpandBtn');
    if (el.classList.contains('news-hidden-collapsed')) {
      el.classList.remove('news-hidden-collapsed');
      btn.classList.add('expanded');
      btn.querySelector('span').textContent = '收起';
    } else {
      el.classList.add('news-hidden-collapsed');
      btn.classList.remove('expanded');
      btn.querySelector('span').textContent = '展开全部（共18篇）';
    }
  }
  ```
- 展开按钮样式：白底圆角药丸，hover蓝边蓝字

### 8. 人才招聘 `#careers`
- 4项福利卡片（薪酬/成长/弹性/健康）
- 岗位列表：2列 `.job-card`（标题+地点+标签+描述）
- 培养计划：4步连线流程

### 9. 常见问题 `#faq`
- 5类 FAQ：购买/使用/售后/海外/企业
- `<details>/<summary>` 手风琴展开

### 10. 使用说明书 `#manuals`
- `.manuals-grid` 自适应网格
- 下载卡片（图标+型号+下载按钮）

### 11. 联系我们 `#contact`
- 左信息 + 右表单（姓名/公司/邮箱/咨询类型/留言 → 提交）
- 联系信息：地址、邮箱、电话、微信

### 12. Footer
- 深蓝底 `#0A2540`
- 4列：品牌介绍 + 产品/服务/联系
- 底部：备案号 + 证书认证链接

---

## 五、新闻列表状态

当前18篇新闻，时间线：
```
2021-10  公司成立
2022-03  制氧机注册证
2022-08  网式雾化器获批
2022-09  洗鼻器获批
2022-11  CMD认证
2023-05  越南MOH注册证      ← 可见分界线（前6篇可见）
─────────────────────────  ← 折叠线
2023-09  泰国TFDA注册
2024-03  二期生产基地投产
2024-04  新标准制氧机首证
2024-04-11  CMEF 89上海
2024-07  BSI-MDR启动
2025-04  江苏省民营科技企业
2025-05  CMEF 2025
2025-06  国家科技型中小企业
2025-09  BSI ISO 13485
2025-11  X500CW上市
2026-04  CMEF 2026
2026-05  呼吸机注册证
```

新闻卡片ID规则：年月 → `202605`，多篇同月 → `20260418`（加日）

---

## 六、部署

- CloudStudio 沙箱：`ef6d0e6ce87242f1b53f1885cc34cbe8`
- 访问地址：`https://ef6d0e6ce87242f1b53f1885cc34cbe8.app.codebuddy.work`
- 部署命令：将 `C:\Users\Administrator\WorkBuddy\Claw\xingmi-website` 目录上传

---

## 七、关键交互

| 功能 | 实现方式 |
|-----|---------|
| 导航激活态高亮 | 滚动监听 + `.active` 类 |
| 产品Tab切换 | `.cat-tab` 点击切换 `.cat-panel` display |
| 视频弹窗 | `.video-modal` + `<video>` 播放 |
| 新闻展开/收起 | `toggleNews()` 切换 `.news-hidden-collapsed` |
| 新闻详情 | URL参数 `?id=xxx` → `newsData[id]` 渲染 |
| 证书灯箱 | `.cert-overlay` + 大图展示 |
| 表单提交 | `Formspree` 服务 |
