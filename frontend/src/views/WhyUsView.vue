<script setup lang="ts">
import { RouterLink } from 'vue-router'

const problems = [
  {
    number: '01',
    title: 'Generic MBA Curricula',
    description:
      'Traditional MBA programs spread thin across marketing, operations, and strategy. Finance gets a handful of electives, not the depth that capital markets, private equity, or asset management demand. Graduates enter the industry with breadth but without the precision firms actually need.',
  },
  {
    number: '02',
    title: 'Theory Without Markets',
    description:
      'Case studies from 2008 taught in 2027. Valuation models built in spreadsheets that never touch live data. The gap between academic finance and how capital actually moves has never been wider. Students learn to pass exams, not to price risk.',
  },
  {
    number: '03',
    title: 'The Employer Ramp-Up Tax',
    description:
      'Banks and funds spend 6 to 12 months retraining new hires. Modelling conventions, deal processes, regulatory nuance, client communication — none of it transfers from a lecture hall. Employers pay the cost. Graduates pay in lost momentum.',
  },
]

const pillars = [
  {
    title: 'Industry Co-Creation',
    description:
      'Every module designed alongside practitioners from leading banks, funds, and advisory firms. The curriculum isn’t inspired by industry — it’s built by it.',
  },
  {
    title: 'Practitioner Faculty',
    description:
      'Our classrooms are led by professionals who close deals, manage portfolios, and advise boards. No full-time academics teaching finance from textbooks.',
  },
  {
    title: 'Immersive Projects',
    description:
      'Live deal simulations, real financial models, actual market data. Students don’t study case histories — they build the muscle memory that Day-1 performance requires.',
  },
  {
    title: 'Career Architecture',
    description:
      'Structured mentorship, industry networking, and placement support designed as a 12-month arc — not an afterthought bolted onto the final term.',
  },
]
</script>

<template>
  <div>
    <!-- Hero -->
    <section class="relative bg-navy pt-32 pb-24 md:pb-32 overflow-hidden">
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--color-navy-light)_0%,_transparent_60%)]" />
      <div class="absolute top-20 right-0 w-96 h-96 bg-gold/5 rounded-full blur-3xl" />

      <div class="relative max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl">
          <div class="inline-flex items-center gap-2 mb-8">
            <span class="w-8 h-px bg-gold" />
            <span class="text-gold text-sm tracking-widest uppercase font-medium">Why Aureum</span>
          </div>

          <h1 class="font-display text-4xl md:text-5xl lg:text-6xl text-white font-bold leading-tight mb-8">
            Finance Education,
            <span class="text-gold">Reimagined</span>
          </h1>

          <p class="text-lg md:text-xl text-slate leading-relaxed max-w-2xl">
            Traditional MBA programs were never designed to produce Day-1 ready finance
            professionals. The industry has evolved. Education hasn't. Until now.
          </p>
        </div>
      </div>
    </section>

    <!-- The Problem -->
    <section class="py-24 md:py-32 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mb-20">
          <span class="text-gold text-sm tracking-widest uppercase font-medium">The Problem</span>
          <h2 class="font-display text-3xl md:text-4xl text-navy font-bold mt-4 mb-6">
            Why the Status Quo Fails
          </h2>
          <p class="text-lg text-charcoal/70 leading-relaxed">
            The finance industry demands precision, speed, and deep technical fluency.
            Most graduate programs deliver none of these.
          </p>
        </div>

        <div class="space-y-20 md:space-y-28">
          <div
            v-for="(problem, index) in problems"
            :key="problem.number"
            class="grid md:grid-cols-2 gap-12 md:gap-16 items-center"
          >
            <div :class="index % 2 === 1 ? 'md:order-2' : ''">
              <div class="flex items-start gap-6">
                <span class="text-6xl md:text-7xl font-display font-bold text-gold/20 leading-none select-none shrink-0">
                  {{ problem.number }}
                </span>
                <div>
                  <h3 class="font-display text-2xl md:text-3xl text-navy font-bold mb-4">
                    {{ problem.title }}
                  </h3>
                  <p class="text-charcoal/70 leading-relaxed text-lg">
                    {{ problem.description }}
                  </p>
                </div>
              </div>
            </div>

            <div :class="index % 2 === 1 ? 'md:order-1' : ''">
              <div class="bg-white rounded-2xl p-8 md:p-10 shadow-sm border border-charcoal/5">
                <div class="w-full h-48 bg-gradient-to-br from-navy/5 to-gold/5 rounded-xl flex items-center justify-center">
                  <span class="text-8xl font-display font-bold text-gold/15">{{ problem.number }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- The Aureum Model -->
    <section class="py-24 md:py-32 bg-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="text-center max-w-3xl mx-auto mb-20">
          <span class="text-gold text-sm tracking-widest uppercase font-medium">Our Approach</span>
          <h2 class="font-display text-3xl md:text-4xl text-navy font-bold mt-4 mb-6">
            A New Operating System for Finance Education
          </h2>
          <p class="text-lg text-charcoal/70 leading-relaxed">
            Aureum is built on four pillars that fundamentally rethink how finance
            professionals are developed — from admission to placement and beyond.
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-8 lg:gap-10">
          <div
            v-for="pillar in pillars"
            :key="pillar.title"
            class="group relative bg-off-white rounded-2xl p-8 md:p-10 border border-charcoal/5 hover:border-gold/30 transition-all duration-300 hover:shadow-lg"
          >
            <div class="absolute top-0 left-8 md:left-10 w-12 h-1 bg-gold rounded-full" />
            <h3 class="font-display text-xl md:text-2xl text-navy font-bold mt-4 mb-4">
              {{ pillar.title }}
            </h3>
            <p class="text-charcoal/70 leading-relaxed">
              {{ pillar.description }}
            </p>
            <div class="mt-6 flex items-center gap-2 text-gold opacity-0 group-hover:opacity-100 transition-opacity duration-300">
              <span class="text-sm font-medium">Learn more</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Vision Statement -->
    <section class="py-24 md:py-32 bg-navy relative overflow-hidden">
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--color-navy-light)_0%,_transparent_70%)]" />
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-gold/3 rounded-full blur-3xl" />

      <div class="relative max-w-5xl mx-auto px-6 lg:px-8 text-center">
        <div class="w-16 h-px bg-gold mx-auto mb-12" />

        <blockquote class="font-display text-3xl md:text-4xl lg:text-5xl text-white italic leading-snug font-medium">
          &ldquo;We don&rsquo;t teach finance.<br class="hidden md:block" />
          We build finance professionals.&rdquo;
        </blockquote>

        <div class="mt-10 flex items-center justify-center gap-3">
          <span class="w-8 h-px bg-gold/50" />
          <span class="text-gold/70 text-sm tracking-widest uppercase">The Aureum Promise</span>
          <span class="w-8 h-px bg-gold/50" />
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-24 md:py-32 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8 text-center">
        <h2 class="font-display text-3xl md:text-4xl text-navy font-bold mb-6">
          Ready to Explore the Program?
        </h2>
        <p class="text-lg text-charcoal/70 mb-10 max-w-2xl mx-auto">
          Discover how the Post Graduate Program in Finance is structured to produce
          professionals the industry actually needs.
        </p>
        <RouterLink
          to="/program"
          class="inline-flex items-center gap-3 bg-gold hover:bg-gold-dark text-navy font-semibold px-8 py-4 rounded-lg transition-colors text-lg"
        >
          Explore the Program
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
          </svg>
        </RouterLink>
      </div>
    </section>
  </div>
</template>
