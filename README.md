<h1 align="center">José Luiz Mendes</h1>

<p align="center">
  <strong>Software Engineer · Web Developer</strong><br/>
  Construo aplicações web e conecto sistemas que não foram feitos para conversar.
</p>

<p align="center">
  <a href="https://mende-shift.vercel.app">
    <img src="https://img.shields.io/badge/Portfólio-mende--shift-3b82f6?style=for-the-badge&labelColor=020617&logo=vercel&logoColor=white" alt="Portfólio"/>
  </a>
  <a href="https://www.linkedin.com/in/SEU-SLUG-AQUI/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="mailto:josemendess004@gmail.com">
    <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
</p>

---

### Sobre

Desenvolvedor full stack desde 2024. Hoje na **TOTVS**, respondo pela conta de um cliente corporativo de transportes e logística: a plataforma web que a operação usa, as automações em n8n que movem os processos e a integração com o ERP Protheus, que concentra os dados do negócio. Trabalho do levantamento de requisitos ao deploy em produção.

Antes, no **Prodest**, atuei em sistemas estruturantes do Governo do Espírito Santo, com foco em qualidade de código, modernização de legado e APIs em C#/.NET.

Gosto de entrar cedo nas discussões técnicas: entender o problema do negócio antes de abrir o editor, levantar o que pode quebrar e deixar registrado o que descobri para quem vier depois.

**Três resultados que carrego:**

| | |
|---|---|
| **−40%** | no prazo de entrega do RAÍZES, sucessor do SIARHES (gestão de pessoas com mais de 95 mil vínculos do estado), com o roadmap de modernização que desenhei — replicado em um projeto de Santa Catarina |
| **Nota A** | no SonarQube em 100% dos repositórios auditados, como líder técnico da governança de código do Portal do Servidor |
| **99/100** | de Real Experience Score em aplicação Next.js medida com usuários reais: 8 ms ao primeiro toque, zero layout shift, TTFB de 0,03 s |

---

### Como eu trabalho

Três coisas aparecem em todo projeto meu, e são o que eu levaria para um time:

- **Teste antes do commit.** Vitest ou Jest no unitário, Playwright no end-to-end, com husky e lint-staged barrando o que não deveria entrar no repositório.
- **Regra escrita, não combinada.** Cada projeto carrega um documento de diretrizes versionado — stack permitida, armadilhas conhecidas, quality gate. Quando o agente ou outro dev abre o repo, as regras estão lá.
- **Decisão com motivo.** Escolher entre dois caminhos e registrar por quê. É o que separa código que sobrevive de código que alguém reescreve em seis meses.

---

### Stack

**No dia a dia**
`TypeScript` `Next.js 16` `React 19` `Node.js` `Fastify` `PostgreSQL` `Prisma` `Drizzle` `Zod` `Tailwind CSS 4` `Docker`

**Em produção, profissionalmente**
`C#` `.NET` `ASP.NET` `n8n` `ERP Protheus (ADVPL)` `Azure DevOps` `SonarQube`

**Qualidade**
`Vitest` `Jest` `Playwright` `Testing Library` — unitário, integração e end-to-end · `ESLint` `Prettier` `Husky`

**Também já usei**
`Java` `Spring Boot` `Vue.js` `Python` `MongoDB` `GraphQL`

---

### Projetos

#### [BipDay](https://github.com/JoseLuizMendes/rotina-app) — PWA de organização pessoal para pessoas com TDAH
`Next.js 16` `React 19` `Prisma 7` `Neon Postgres` `Auth.js v5` `Serwist` `Web Push` `Zustand` `Vitest` `Playwright`

O diferencial não é mais uma lista de tarefas: é o **bip** — o alerta de transição que avisa pouco antes de cada bloco começar, porque a dificuldade costuma não ser saber o que fazer, e sim trocar de contexto na hora certa. Timer visível e sequência sem punição: falhar não pinta nada de vermelho.

Tecnicamente: PWA instalável com service worker gerado no build (Serwist) e notificações Web Push com VAPID, multi-tenant por username, autenticação com Auth.js v5 em sessão JWT, Prisma 7 com adapter-pg sobre Neon, e recorrência de blocos com RRULE. Testes em dois níveis e design system documentado em `DESIGN.md`. Em dogfooding antes de ir a mercado.

#### [Clínica Dr. Gabriel Cavalcanti](https://github.com/JoseLuizMendes/dr-gabriel-cavalcante-web) — Sistema de gestão odontológica
`Next.js 16` `React 19` `TanStack Query` `Drizzle ORM` `Neon Postgres` `Tailwind 4` `FullCalendar` `Recharts` `Playwright`

Site público da clínica e hub da equipe para agenda, pacientes, prontuário e faturamento. Sem cadastro público: acessos (`OWNER`/`STAFF`) são criados pelo próprio OWNER.

Decisões que valem citar: **fetch via React Query por regra de projeto — `useEffect` para buscar dados é proibido**; sessão em cookie httpOnly definido pela API, nunca lida pelo JS; cores só por token, zero hex no código; Error Boundaries do App Router com fallback amigável e `reset()`; a11y com `focus-visible`, `aria-pressed` e `prefers-reduced-motion`. O site é mobile-first porque o paciente chega pelo celular; o hub é desktop-first porque a recepção opera em desktop o dia inteiro — e ambos são responsivos.

Os E2E rodam em quatro projetos encadeados (reset do banco → login pela UI → hub), com um banco de testes que **recusa qualquer escrita em base sem a marcadora de segurança**.

#### [My Wedding](https://github.com/JoseLuizMendes/My-Wedding-New) — Plataforma de casamento · *em produção*
`Next.js` `TypeScript` `Prisma` `Neon` `Mercado Pago` `Vercel Blob` `Jest` `Playwright`

Confirmação de presença para dois eventos, lista de presentes com sistema de reserva e fundo de lua de mel com checkout e webhooks do Mercado Pago. Autenticação de convidado por código OTP, upload de fotos com compressão no browser antes de subir para o Vercel Blob, e e-mail transacional com nodemailer.

Usuários, pagamentos e uploads reais — foi o site do meu próprio casamento, o que torna cada bug um problema de verdade.

#### [Belessence](https://github.com/JoseLuizMendes/Belessence) — E-commerce de cosméticos · *cliente real*
`Next.js` `React` `TypeScript` `Prisma` `PostgreSQL` `Tailwind CSS`

Catálogo com filtros, carrinho com estado persistente, checkout e painel de gestão de pedidos. UI baseada em componentes para que a proprietária atualize o catálogo sem conhecimento técnico. Mobile-first, adequado a uma marca com aquisição por redes sociais.

#### [MendeShift](https://github.com/JoseLuizMendes/Mendeshift) — Portfólio e estúdio de desenvolvimento web
`Next.js 16` `React 19` `React Compiler` `Tailwind 4` `GSAP` `Lenis` `next-intl` `MDX` `Upstash` `Resend`

Real Experience Score de 99/100 no Vercel Speed Insights, medido com usuários reais: 8 ms ao primeiro toque, zero layout shift, TTFB de 0,03 s. GSAP e Lenis em vez de biblioteca de scroll pronta para reduzir bundle, coordenação entre componentes por eventos de DOM sem contexto global, i18n com next-intl e build Docker multi-stage com output standalone.

Blog em MDX com realce de sintaxe via Shiki, formulário de contato com rate limiting em Upstash Redis e envio por Resend.

---

### Estudando agora

Kubernetes, mensageria com RabbitMQ e Kafka, e AWS. Mantenho os projetos acima como laboratório porque errar ali é barato e me deixa mais preparado na hora de decidir em produção.

---

<p align="center">
  <a href="https://mende-shift.vercel.app">Portfólio</a> ·
  <a href="https://www.linkedin.com/in/SEU-SLUG-AQUI/">LinkedIn</a> ·
  <a href="mailto:josemendess004@gmail.com">josemendess004@gmail.com</a>
</p>
