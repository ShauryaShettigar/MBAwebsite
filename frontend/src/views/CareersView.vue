<script setup lang="ts">
import { RouterLink } from 'vue-router'

const pillars = [
  {
    title: 'Technical Mastery',
    description:
      'Deep proficiency in financial modelling, valuation, risk analysis, and data-driven decision making — built through relentless case work and live projects.',
    icon: 'M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z',
  },
  {
    title: 'Professional Maturity',
    description:
      'Communication, leadership, and ethical judgement honed through boardroom simulations, client presentations, and team-based deal execution.',
    icon: 'M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z',
  },
  {
    title: 'Industry Network',
    description:
      'From day one, students engage with practitioners, attend closed-door industry sessions, and build relationships that open doors long after graduation.',
    icon: 'M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582m15.686 0A11.953 11.953 0 0112 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0121 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0112 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 013 12c0-1.605.42-3.113 1.157-4.418',
  },
]

const roles = [
  {
    title: 'Investment Banking Analyst',
    description:
      'Execute deal origination, financial modelling, and client advisory at top-tier banks and boutique firms.',
    salary: '18 – 28L',
  },
  {
    title: 'Asset Management Associate',
    description:
      'Research-driven equity and fixed-income portfolio management across mutual funds, AIFs, and family offices.',
    salary: '15 – 25L',
  },
  {
    title: 'Private Equity Associate',
    description:
      'Source deals, conduct due diligence, and support portfolio companies at growth and buyout funds.',
    salary: '20 – 30L',
  },
  {
    title: 'Fintech Product Manager',
    description:
      'Define product strategy at the intersection of finance and technology — payments, lending, wealthtech, and insurtech.',
    salary: '18 – 28L',
  },
  {
    title: 'Corporate Finance Manager',
    description:
      'Lead treasury, FP&A, and strategic finance functions inside high-growth companies and conglomerates.',
    salary: '15 – 24L',
  },
  {
    title: 'Risk & Compliance Analyst',
    description:
      'Build and monitor risk frameworks, regulatory reporting, and compliance systems at banks and NBFCs.',
    salary: '14 – 22L',
  },
]

const employers = [
  { name: 'Goldman Sachs', category: 'Global Bank', logo: '/logos/goldman-sachs.svg' },
  { name: 'JP Morgan', category: 'Global Bank', logo: '/logos/jpmorgan.svg' },
  { name: 'HDFC Bank', category: 'Private Bank', logo: '/logos/hdfc-bank.svg' },
  { name: 'ICICI Bank', category: 'Private Bank', logo: '/logos/icici-bank.svg' },
  { name: 'Kotak Mahindra', category: 'Private Bank', logo: '/logos/kotak.svg' },
  { name: 'Axis Bank', category: 'Private Bank', logo: '/logos/axis-bank.svg' },
  { name: 'Bajaj Finserv', category: 'Financial Services', logo: '/logos/bajaj-finserv.svg' },
  { name: 'Edelweiss', category: 'Wealth Management', logo: '/logos/edelweiss.svg' },
  { name: 'Avendus', category: 'Investment Bank', logo: '/logos/avendus.svg' },
  { name: 'PhonePe', category: 'Fintech', logo: '/logos/phonepe.svg' },
  { name: 'CRED', category: 'Fintech', logo: '/logos/cred.svg' },
  { name: 'Razorpay', category: 'Fintech', logo: '/logos/razorpay.svg' },
]

const supportItems = [
  {
    title: 'Dedicated Career Services',
    description:
      'A full-time career strategy team works with every student from orientation through offer acceptance — not a placement cell, a career partnership.',
  },
  {
    title: 'Mock Interviews & Case Prep',
    description:
      'Rigorous simulation of technical rounds, HR interviews, and case competitions with feedback from practitioners who have sat on the other side.',
  },
  {
    title: 'Resume & Profile Workshops',
    description:
      'Craft a professional narrative that positions you for the roles you want — résumé, LinkedIn, cover letters, and personal branding.',
  },
  {
    title: 'Industry Networking Events',
    description:
      'Exclusive meet-and-greet sessions, panel discussions, and closed-door dinners with hiring managers, fund managers, and founders.',
  },
  {
    title: 'Alumni Mentorship Program',
    description:
      'Every student is paired with a senior finance professional who provides guidance on career decisions, skill gaps, and long-term growth.',
  },
]
</script>

<template>
  <div>
    <!-- Hero -->
    <section class="bg-navy pt-32 pb-20 lg:pb-28 relative overflow-hidden">
      <div
        class="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--color-navy-light)_0%,_transparent_60%)]"
      />
      <div class="max-w-7xl mx-auto px-6 lg:px-8 relative">
        <div class="max-w-3xl">
          <p
            class="text-gold uppercase tracking-[0.2em] text-xs font-semibold mb-6"
          >
            Career Outcomes
          </p>
          <h1
            class="font-display text-4xl md:text-5xl lg:text-6xl font-bold text-white leading-tight mb-6"
          >
            Careers That Start
            <span class="text-gold">on Day One</span>
          </h1>
          <p class="text-white/60 text-lg lg:text-xl leading-relaxed max-w-2xl">
            Aureum graduates don't just find jobs — they arrive prepared to
            create impact. Our program is engineered so that the distance
            between your last class and your first board meeting is as short as
            possible.
          </p>
        </div>
      </div>
    </section>

    <!-- Career Readiness Philosophy -->
    <section class="py-20 lg:py-28 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mx-auto text-center mb-16">
          <p
            class="text-gold-dark uppercase tracking-[0.2em] text-xs font-semibold mb-4"
          >
            Our Philosophy
          </p>
          <h2
            class="font-display text-3xl md:text-4xl font-bold text-charcoal mb-6"
          >
            Day-1 Ready Is Not a Slogan
          </h2>
          <p class="text-slate text-lg leading-relaxed">
            Most business schools measure success by placement percentages. We
            measure it by how quickly our graduates earn the trust of their
            teams. Every element of the Aureum experience — from live deal
            simulations to mentorship by practitioners — is designed to close
            the gap between classroom and career.
          </p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
          <div
            v-for="pillar in pillars"
            :key="pillar.title"
            class="bg-white rounded-xl p-8 shadow-sm border border-black/5 hover:shadow-md transition-shadow"
          >
            <div
              class="w-12 h-12 rounded-lg bg-gold/10 flex items-center justify-center mb-6"
            >
              <svg
                class="w-6 h-6 text-gold-dark"
                fill="none"
                stroke="currentColor"
                stroke-width="1.5"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  :d="pillar.icon"
                />
              </svg>
            </div>
            <h3 class="font-display text-xl font-semibold text-charcoal mb-3">
              {{ pillar.title }}
            </h3>
            <p class="text-slate text-sm leading-relaxed">
              {{ pillar.description }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Target Roles -->
    <section class="py-20 lg:py-28 bg-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mx-auto text-center mb-16">
          <p
            class="text-gold-dark uppercase tracking-[0.2em] text-xs font-semibold mb-4"
          >
            Career Paths
          </p>
          <h2
            class="font-display text-3xl md:text-4xl font-bold text-charcoal mb-6"
          >
            Where Aureum Graduates Lead
          </h2>
          <p class="text-slate text-lg leading-relaxed">
            Our curriculum is mapped to the roles that define modern finance.
            Graduates enter the workforce with skills that employers actively
            seek.
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="role in roles"
            :key="role.title"
            class="group rounded-xl border border-black/5 p-7 hover:border-gold/30 hover:shadow-lg transition-all bg-cream/50"
          >
            <h3
              class="font-display text-lg font-semibold text-charcoal mb-2 group-hover:text-gold-dark transition-colors"
            >
              {{ role.title }}
            </h3>
            <p class="text-slate text-sm leading-relaxed mb-4">
              {{ role.description }}
            </p>
            <div
              class="inline-flex items-center gap-1.5 text-xs font-semibold text-gold-dark bg-gold/10 px-3 py-1.5 rounded-full"
            >
              <span>Indicative CTC</span>
              <span class="text-charcoal">&curren;{{ role.salary }}</span>
            </div>
          </div>
        </div>

        <p class="text-center text-slate/60 text-xs mt-8">
          Salary ranges are indicative and based on current market benchmarks
          for top-tier Indian institutions. Actual offers vary by employer,
          role, and candidate profile.
        </p>
      </div>
    </section>

    <!-- Employer Network -->
    <section class="py-20 lg:py-28 bg-navy">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mx-auto text-center mb-16">
          <p
            class="text-gold uppercase tracking-[0.2em] text-xs font-semibold mb-4"
          >
            Employer Network
          </p>
          <h2
            class="font-display text-3xl md:text-4xl font-bold text-white mb-6"
          >
            Companies Where Our Graduates Will Thrive
          </h2>
          <p class="text-white/50 text-lg leading-relaxed">
            We are building relationships with institutions that value
            substance over pedigree — organisations where talent, preparation,
            and character open the door.
          </p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
          <div
            v-for="employer in employers"
            :key="employer.name"
            class="bg-white/5 border border-white/10 rounded-lg p-6 flex flex-col items-center justify-center text-center hover:bg-white/10 hover:border-gold/20 transition-all group"
          >
            <div
              class="w-14 h-14 rounded-full bg-white flex items-center justify-center mb-3 p-2 group-hover:shadow-lg transition-all"
            >
              <img
                :src="employer.logo"
                :alt="employer.name + ' logo'"
                class="w-10 h-10 object-contain"
                loading="lazy"
              />
            </div>
            <span class="text-white font-medium text-sm">{{
              employer.name
            }}</span>
            <span class="text-white/40 text-xs mt-1">{{
              employer.category
            }}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Career Support -->
    <section class="py-20 lg:py-28 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mx-auto text-center mb-16">
          <p
            class="text-gold-dark uppercase tracking-[0.2em] text-xs font-semibold mb-4"
          >
            Career Support
          </p>
          <h2
            class="font-display text-3xl md:text-4xl font-bold text-charcoal mb-6"
          >
            Your Career, Our Commitment
          </h2>
          <p class="text-slate text-lg leading-relaxed">
            Aureum invests in every student's professional trajectory — not
            just during the program, but well beyond graduation.
          </p>
        </div>

        <div class="space-y-4 max-w-3xl mx-auto">
          <div
            v-for="(item, index) in supportItems"
            :key="item.title"
            class="flex gap-5 bg-white rounded-xl p-6 border border-black/5"
          >
            <div
              class="flex-shrink-0 w-10 h-10 rounded-full bg-gold/10 flex items-center justify-center"
            >
              <span class="text-gold-dark font-display font-bold text-sm">
                {{ String(index + 1).padStart(2, '0') }}
              </span>
            </div>
            <div>
              <h3 class="font-display text-lg font-semibold text-charcoal mb-1">
                {{ item.title }}
              </h3>
              <p class="text-slate text-sm leading-relaxed">
                {{ item.description }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-20 lg:py-28 bg-charcoal relative overflow-hidden">
      <div
        class="absolute inset-0 bg-[radial-gradient(ellipse_at_bottom_left,_var(--color-navy-light)_0%,_transparent_60%)]"
      />
      <div class="max-w-7xl mx-auto px-6 lg:px-8 text-center relative">
        <h2
          class="font-display text-3xl md:text-4xl lg:text-5xl font-bold text-white mb-6"
        >
          Start Your Finance Career
        </h2>
        <p
          class="text-white/50 text-lg leading-relaxed max-w-2xl mx-auto mb-10"
        >
          The founding cohort is forming. If you are ready to commit to a
          career in finance, we are ready to invest in you.
        </p>
        <RouterLink
          to="/admissions"
          class="inline-flex items-center gap-2 bg-gold hover:bg-gold-dark text-navy font-semibold px-8 py-4 rounded text-lg transition-colors"
        >
          Explore Admissions
          <svg
            class="w-5 h-5"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
            />
          </svg>
        </RouterLink>
      </div>
    </section>
  </div>
</template>
