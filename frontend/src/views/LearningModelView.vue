<script setup lang="ts">
import { RouterLink } from 'vue-router'

const comparisons = [
  { traditional: 'Passive lectures', aureum: 'Live case simulations' },
  { traditional: 'Standardized exams', aureum: 'Industry project evaluations' },
  { traditional: 'Professors only', aureum: 'Practitioners + Academics' },
  { traditional: 'Fixed semesters', aureum: 'Modular learning sprints' },
  { traditional: 'Individual assignments', aureum: 'Collaborative case pods' },
]

const coreComponents = [
  {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" /></svg>`,
    title: 'Practitioner-Led Sessions',
    description:
      'Senior finance leaders — from managing directors to portfolio managers — teach directly from decades of lived experience. No secondhand theory, only first-person insight from the industry\'s sharpest minds.',
  },
  {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M18 18.72a9.094 9.094 0 0 0 3.741-.479 3 3 0 0 0-4.682-2.72m.94 3.198.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0 1 12 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 0 1 6 18.719m12 0a5.971 5.971 0 0 0-.941-3.197m0 0A5.995 5.995 0 0 0 12 12.75a5.995 5.995 0 0 0-5.058 2.772m0 0a3 3 0 0 0-4.681 2.72 8.986 8.986 0 0 0 3.74.477m.94-3.197a5.971 5.971 0 0 0-.94 3.197M15 6.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Zm6 3a2.25 2.25 0 1 1-4.5 0 2.25 2.25 0 0 1 4.5 0Zm-13.5 0a2.25 2.25 0 1 1-4.5 0 2.25 2.25 0 0 1 4.5 0Z" /></svg>`,
    title: 'Industry Case Pods',
    description:
      'Small, diverse teams work on real challenges sourced from partner companies. Each pod functions like a junior advisory team, producing deliverables that matter beyond the classroom.',
  },
  {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3v11.25A2.25 2.25 0 0 0 6 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0 1 18 16.5h-2.25m-7.5 0h7.5m-7.5 0-1 3m8.5-3 1 3m0 0 .5 1.5m-.5-1.5h-9.5m0 0-.5 1.5M9 11.25v1.5M12 9v3.75m3-6v6" /></svg>`,
    title: 'Capstone Projects',
    description:
      'Three-month embedded industry projects where students work inside partner organizations on live strategic problems — from M&A analysis to fintech product launches.',
  },
  {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 0 1-.825-.242m9.345-8.334a2.126 2.126 0 0 0-.476-.095 48.64 48.64 0 0 0-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0 0 11.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155" /></svg>`,
    title: 'Peer Learning Circles',
    description:
      'Structured collaboration sessions with a deliberately diverse cohort. Engineers, entrepreneurs, and analysts learn from each other in facilitated discussions that mirror real boardroom dynamics.',
  },
]

const steps = [
  { label: 'Learn', desc: 'Absorb frameworks from practitioners' },
  { label: 'Apply', desc: 'Work on live industry challenges' },
  { label: 'Reflect', desc: 'Synthesize with peers and mentors' },
  { label: 'Master', desc: 'Demonstrate through portfolio outcomes' },
]

const assessmentMethods = [
  {
    title: 'Project Outcomes',
    description: 'Evaluated on the quality and rigor of deliverables produced for real industry partners.',
  },
  {
    title: 'Peer Reviews',
    description: 'Structured 360-degree feedback from pod members assessing collaboration and contribution.',
  },
  {
    title: 'Industry Evaluations',
    description: 'Direct assessment from practitioner faculty and company mentors on professional readiness.',
  },
  {
    title: 'Portfolio Building',
    description: 'A cumulative body of work that demonstrates analytical depth and strategic thinking to future employers.',
  },
]
</script>

<template>
  <div>
    <!-- Hero -->
    <section class="relative bg-navy pt-32 pb-20 lg:pb-28 overflow-hidden">
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--color-navy-light)_0%,_transparent_60%)]" />
      <div class="relative max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl">
          <p class="text-gold text-sm font-semibold tracking-[0.2em] uppercase mb-6">
            Pedagogy
          </p>
          <h1 class="font-display text-4xl md:text-5xl lg:text-6xl text-white font-bold leading-tight mb-6">
            The Learning<br />Operating System
          </h1>
          <p class="text-lg md:text-xl text-slate leading-relaxed max-w-2xl">
            Not a syllabus. A system designed to produce mastery. Every element
            — from who teaches to how you're assessed — is engineered around one
            outcome: making you genuinely ready for the highest levels of finance.
          </p>
        </div>
      </div>
    </section>

    <!-- The Philosophy -->
    <section class="py-20 lg:py-28 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mb-16">
          <p class="text-gold text-sm font-semibold tracking-[0.2em] uppercase mb-4">
            The Philosophy
          </p>
          <h2 class="font-display text-3xl md:text-4xl text-charcoal font-bold mb-6">
            Curriculum is what you study.<br />
            An operating system is how you learn.
          </h2>
          <p class="text-slate text-lg leading-relaxed">
            Traditional programs hand you a reading list and a schedule. The
            Aureum LOS is an integrated architecture — practitioner instruction,
            applied projects, peer synthesis, and industry evaluation — all
            working together to compress the gap between education and expertise.
          </p>
        </div>

        <!-- Comparison Table -->
        <div class="bg-white rounded-2xl shadow-sm border border-charcoal/5 overflow-hidden">
          <!-- Header -->
          <div class="grid grid-cols-2 border-b border-charcoal/10">
            <div class="px-6 lg:px-10 py-5 bg-charcoal/[0.03]">
              <span class="text-sm font-semibold text-slate uppercase tracking-wider">Traditional MBA</span>
            </div>
            <div class="px-6 lg:px-10 py-5 bg-navy">
              <span class="text-sm font-semibold text-gold uppercase tracking-wider">Aureum LOS</span>
            </div>
          </div>
          <!-- Rows -->
          <div
            v-for="(row, i) in comparisons"
            :key="i"
            class="grid grid-cols-2 border-b border-charcoal/5 last:border-b-0"
          >
            <div class="px-6 lg:px-10 py-5 flex items-center text-slate">
              {{ row.traditional }}
            </div>
            <div class="px-6 lg:px-10 py-5 flex items-center text-charcoal font-medium bg-gold/[0.04]">
              {{ row.aureum }}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Core Components -->
    <section class="py-20 lg:py-28 bg-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mb-16">
          <p class="text-gold text-sm font-semibold tracking-[0.2em] uppercase mb-4">
            Core Components
          </p>
          <h2 class="font-display text-3xl md:text-4xl text-charcoal font-bold mb-6">
            Four pillars of the system
          </h2>
          <p class="text-slate text-lg leading-relaxed">
            Each component reinforces the others, creating a compounding learning
            loop that mirrors how expertise is actually built in high-performance
            finance environments.
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-6 lg:gap-8">
          <div
            v-for="component in coreComponents"
            :key="component.title"
            class="group relative bg-off-white rounded-xl p-8 lg:p-10 border-l-4 border-gold transition-all duration-300 hover:shadow-lg hover:shadow-gold/5"
          >
            <div class="text-gold mb-5" v-html="component.icon" />
            <h3 class="font-display text-xl lg:text-2xl text-charcoal font-bold mb-3">
              {{ component.title }}
            </h3>
            <p class="text-slate leading-relaxed">
              {{ component.description }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- How It Works -->
    <section class="py-20 lg:py-28 bg-navy">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="text-center mb-16">
          <p class="text-gold text-sm font-semibold tracking-[0.2em] uppercase mb-4">
            How It Works
          </p>
          <h2 class="font-display text-3xl md:text-4xl text-white font-bold">
            The mastery loop
          </h2>
        </div>

        <!-- Timeline -->
        <div class="relative">
          <!-- Desktop: horizontal -->
          <div class="hidden md:grid md:grid-cols-4 gap-0">
            <div
              v-for="(step, i) in steps"
              :key="step.label"
              class="relative flex flex-col items-center text-center px-6"
            >
              <!-- Connector line -->
              <div
                v-if="i < steps.length - 1"
                class="absolute top-6 left-1/2 w-full h-px bg-gold/30"
              />
              <!-- Circle -->
              <div class="relative z-10 w-12 h-12 rounded-full bg-gold/10 border-2 border-gold flex items-center justify-center mb-5">
                <span class="text-gold font-display font-bold text-lg">{{ i + 1 }}</span>
              </div>
              <h3 class="font-display text-xl text-white font-bold mb-2">
                {{ step.label }}
              </h3>
              <p class="text-slate text-sm leading-relaxed">
                {{ step.desc }}
              </p>
            </div>
          </div>

          <!-- Mobile: vertical -->
          <div class="md:hidden space-y-8">
            <div
              v-for="(step, i) in steps"
              :key="step.label"
              class="relative flex items-start gap-5"
            >
              <!-- Vertical line -->
              <div class="flex flex-col items-center">
                <div class="w-10 h-10 rounded-full bg-gold/10 border-2 border-gold flex items-center justify-center shrink-0">
                  <span class="text-gold font-display font-bold">{{ i + 1 }}</span>
                </div>
                <div v-if="i < steps.length - 1" class="w-px flex-1 bg-gold/30 mt-2" />
              </div>
              <div class="pb-6">
                <h3 class="font-display text-lg text-white font-bold mb-1">
                  {{ step.label }}
                </h3>
                <p class="text-slate text-sm leading-relaxed">
                  {{ step.desc }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Assessment Model -->
    <section class="py-20 lg:py-28 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mb-16">
          <p class="text-gold text-sm font-semibold tracking-[0.2em] uppercase mb-4">
            Assessment Model
          </p>
          <h2 class="font-display text-3xl md:text-4xl text-charcoal font-bold mb-6">
            Prove mastery. Not memorization.
          </h2>
          <p class="text-slate text-lg leading-relaxed">
            There are no traditional exams at Aureum. You are assessed the way
            the industry assesses — through the quality of your thinking, your
            ability to deliver under constraints, and your readiness to add
            value from day one.
          </p>
        </div>

        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div
            v-for="method in assessmentMethods"
            :key="method.title"
            class="bg-white rounded-xl p-7 border border-charcoal/5"
          >
            <div class="w-10 h-10 rounded-lg bg-gold/10 flex items-center justify-center mb-5">
              <div class="w-3 h-3 rounded-full bg-gold" />
            </div>
            <h3 class="font-display text-lg text-charcoal font-bold mb-2">
              {{ method.title }}
            </h3>
            <p class="text-slate text-sm leading-relaxed">
              {{ method.description }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-20 lg:py-28 bg-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8 text-center">
        <h2 class="font-display text-3xl md:text-4xl text-charcoal font-bold mb-4">
          See how the system comes together
        </h2>
        <p class="text-slate text-lg mb-10 max-w-2xl mx-auto">
          Explore the full program structure — modules, timelines, and how every
          component of the Learning OS maps to your career trajectory.
        </p>
        <RouterLink
          to="/program"
          class="inline-flex items-center gap-2 bg-gold hover:bg-gold-dark text-navy font-semibold px-8 py-4 rounded transition-colors text-lg"
        >
          See the Program Structure
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
          </svg>
        </RouterLink>
      </div>
    </section>
  </div>
</template>
