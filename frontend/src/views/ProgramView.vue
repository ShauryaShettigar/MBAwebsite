<script setup lang="ts">
import { RouterLink } from 'vue-router'

const snapshot = [
  { label: 'Duration', value: '12 Months', detail: 'Intensive, full-time' },
  { label: 'Format', value: 'Full-Time', detail: 'Mumbai campus' },
  { label: 'Cohort Size', value: '60 Students', detail: 'Founding batch' },
  { label: 'Pedagogy', value: '100%', detail: 'Practitioner-led' },
]

const profiles = [
  {
    title: 'Investment Banking Aspirants',
    description:
      'Analysts and associates looking to deepen their modelling, deal execution, and client advisory skills before moving to bulge-bracket or elite boutique roles.',
    tags: ['IB', 'M&A', 'DCM / ECM'],
  },
  {
    title: 'Private Equity & Venture Capital',
    description:
      'Professionals targeting buy-side roles who need rigorous training in LBO modelling, portfolio operations, due diligence, and fund-level thinking.',
    tags: ['PE', 'VC', 'Growth Equity'],
  },
  {
    title: 'Asset & Wealth Management',
    description:
      'Individuals drawn to portfolio construction, risk management, and client-facing advisory across public and alternative asset classes.',
    tags: ['AM', 'HF', 'Multi-Asset'],
  },
  {
    title: 'Fintech & Structured Finance',
    description:
      'Builders and operators at the intersection of technology and financial markets — from credit platforms to digital assets infrastructure.',
    tags: ['Fintech', 'Structured Products', 'Digital Assets'],
  },
]

const phases = [
  {
    phase: 'Phase I',
    title: 'Foundation',
    months: 'Months 1–3',
    description:
      'Build an unshakable base in financial accounting, corporate finance, quantitative methods, and the mechanics of capital markets. Every student reaches the same rigorous baseline, regardless of background.',
    accent: 'bg-gold/10 border-gold/20',
  },
  {
    phase: 'Phase II',
    title: 'Specialization',
    months: 'Months 4–8',
    description:
      'Dive deep into your chosen track — Investment Banking, Private Equity, Asset Management, or Fintech. Practitioner-led modules, live deal case studies, and intensive modelling workshops replace traditional lectures.',
    accent: 'bg-gold/15 border-gold/25',
  },
  {
    phase: 'Phase III',
    title: 'Industry Immersion',
    months: 'Months 9–12',
    description:
      'Capstone industry projects embedded with partner firms. Real mandates, real clients, real deliverables. This isn’t a summer internship — it’s a four-month proving ground that ends with a placement-ready portfolio.',
    accent: 'bg-gold/20 border-gold/30',
  },
]

const philosophyPoints = [
  {
    title: 'Industry-Designed Modules',
    description: 'Curriculum shaped by practitioners from leading financial institutions, updated every cohort to reflect how the industry actually operates.',
  },
  {
    title: 'Live Deal Case Studies',
    description: 'Forget hypotheticals. Students work with real transaction data, actual market events, and live financial models pulled from recent deals.',
  },
  {
    title: 'Practitioner Mentorship',
    description: 'Every student is paired with a senior finance professional who guides their development through the full 12-month arc.',
  },
  {
    title: 'Capstone Industry Projects',
    description: 'The final four months are spent embedded with partner firms on real mandates — producing work that matters, not academic exercises.',
  },
]
</script>

<template>
  <div>
    <!-- Hero -->
    <section class="relative bg-navy pt-32 pb-24 md:pb-32 overflow-hidden">
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top_left,_var(--color-navy-light)_0%,_transparent_60%)]" />
      <div class="absolute bottom-0 right-0 w-80 h-80 bg-gold/5 rounded-full blur-3xl" />

      <div class="relative max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl">
          <div class="inline-flex items-center gap-3 mb-8">
            <span class="bg-gold/10 border border-gold/30 text-gold text-xs font-semibold tracking-wider uppercase px-4 py-1.5 rounded-full">
              Launching June 2027
            </span>
          </div>

          <h1 class="font-display text-4xl md:text-5xl lg:text-6xl text-white font-bold leading-tight mb-8">
            Post Graduate Program
            <span class="block text-gold">in Finance</span>
          </h1>

          <p class="text-lg md:text-xl text-slate leading-relaxed max-w-2xl">
            A 12-month, full-time program designed from the ground up to produce
            Day-1 ready finance professionals — not generalist MBAs who need
            another year of on-the-job training.
          </p>
        </div>
      </div>
    </section>

    <!-- Program Snapshot -->
    <section class="py-24 md:py-28 bg-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="text-center mb-16">
          <span class="text-gold text-sm tracking-widest uppercase font-medium">At a Glance</span>
          <h2 class="font-display text-3xl md:text-4xl text-navy font-bold mt-4">
            Program Snapshot
          </h2>
        </div>

        <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 lg:gap-8">
          <div
            v-for="item in snapshot"
            :key="item.label"
            class="text-center bg-off-white rounded-2xl p-8 border border-charcoal/5"
          >
            <p class="text-sm text-charcoal/50 uppercase tracking-wider mb-3">{{ item.label }}</p>
            <p class="font-display text-2xl md:text-3xl text-navy font-bold mb-2">{{ item.value }}</p>
            <p class="text-sm text-charcoal/60">{{ item.detail }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Who Is It For -->
    <section class="py-24 md:py-32 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mb-16">
          <span class="text-gold text-sm tracking-widest uppercase font-medium">Ideal Candidates</span>
          <h2 class="font-display text-3xl md:text-4xl text-navy font-bold mt-4 mb-6">
            Who Is This Program For?
          </h2>
          <p class="text-lg text-charcoal/70 leading-relaxed">
            Aureum is designed for ambitious professionals and graduates who know they want
            to build a career in finance — and want to arrive prepared, not just credentialed.
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-8">
          <div
            v-for="profile in profiles"
            :key="profile.title"
            class="bg-white rounded-2xl p-8 md:p-10 border border-charcoal/5 hover:border-gold/20 hover:shadow-md transition-all duration-300"
          >
            <h3 class="font-display text-xl text-navy font-bold mb-3">
              {{ profile.title }}
            </h3>
            <p class="text-charcoal/70 leading-relaxed mb-6">
              {{ profile.description }}
            </p>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="tag in profile.tags"
                :key="tag"
                class="bg-navy/5 text-navy/70 text-xs font-medium px-3 py-1 rounded-full"
              >
                {{ tag }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Curriculum Philosophy -->
    <section class="py-24 md:py-32 bg-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="grid lg:grid-cols-2 gap-16 items-start">
          <div class="lg:sticky lg:top-32">
            <span class="text-gold text-sm tracking-widest uppercase font-medium">Curriculum Philosophy</span>
            <h2 class="font-display text-3xl md:text-4xl text-navy font-bold mt-4 mb-6">
              Built Around Real Finance,
              <span class="text-gold">Not Textbook Finance</span>
            </h2>
            <p class="text-lg text-charcoal/70 leading-relaxed">
              We don't publish a rigid course catalogue. Our curriculum is a living system — shaped
              by industry partners, updated every cohort, and anchored in the skills that
              employers actually test for.
            </p>
          </div>

          <div class="space-y-6">
            <div
              v-for="(point, index) in philosophyPoints"
              :key="point.title"
              class="relative pl-8 border-l-2 border-gold/20 hover:border-gold transition-colors duration-300"
            >
              <div class="absolute left-0 top-1 w-2 h-2 bg-gold rounded-full -translate-x-[5px]" />
              <h3 class="font-display text-lg text-navy font-bold mb-2">
                {{ point.title }}
              </h3>
              <p class="text-charcoal/70 leading-relaxed">
                {{ point.description }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Learning Experience / Phases -->
    <section class="py-24 md:py-32 bg-navy relative overflow-hidden">
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_bottom_left,_var(--color-navy-light)_0%,_transparent_60%)]" />

      <div class="relative max-w-7xl mx-auto px-6 lg:px-8">
        <div class="text-center max-w-3xl mx-auto mb-20">
          <span class="text-gold text-sm tracking-widest uppercase font-medium">The Journey</span>
          <h2 class="font-display text-3xl md:text-4xl text-white font-bold mt-4 mb-6">
            12 Months, Three Phases
          </h2>
          <p class="text-lg text-slate leading-relaxed">
            A deliberately sequenced learning arc that builds from fundamentals to
            specialization to full industry immersion.
          </p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
          <div
            v-for="(phase, index) in phases"
            :key="phase.phase"
            class="relative bg-white/5 backdrop-blur-sm rounded-2xl p-8 md:p-10 border border-white/10 hover:border-gold/30 transition-all duration-300"
          >
            <div class="absolute top-0 left-8 md:left-10 right-8 md:right-10 h-px bg-gradient-to-r from-gold/50 via-gold/20 to-transparent" />

            <div class="flex items-center gap-3 mb-6 mt-2">
              <span class="text-gold font-display text-sm font-semibold tracking-wider uppercase">
                {{ phase.phase }}
              </span>
              <span class="w-6 h-px bg-white/20" />
              <span class="text-white/40 text-sm">{{ phase.months }}</span>
            </div>

            <h3 class="font-display text-2xl text-white font-bold mb-4">
              {{ phase.title }}
            </h3>

            <p class="text-slate leading-relaxed">
              {{ phase.description }}
            </p>

            <div class="mt-8 flex items-center gap-2">
              <div
                v-for="dot in 3"
                :key="dot"
                class="w-2 h-2 rounded-full"
                :class="dot <= index + 1 ? 'bg-gold' : 'bg-white/15'"
              />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Founding Cohort Advantage -->
    <section class="py-24 md:py-32 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-5xl mx-auto">
          <div class="relative bg-navy rounded-3xl p-10 md:p-16 overflow-hidden">
            <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--color-navy-light)_0%,_transparent_70%)]" />
            <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-gold via-gold-light to-gold" />
            <div class="absolute -bottom-20 -right-20 w-64 h-64 bg-gold/5 rounded-full blur-3xl" />

            <div class="relative">
              <div class="inline-flex items-center gap-2 mb-6">
                <span class="w-8 h-px bg-gold" />
                <span class="text-gold text-sm tracking-widest uppercase font-medium">Founding Cohort</span>
              </div>

              <h2 class="font-display text-3xl md:text-4xl text-white font-bold mb-8">
                Shape the Institution's Legacy
              </h2>

              <div class="grid md:grid-cols-3 gap-8 md:gap-10">
                <div>
                  <div class="w-12 h-12 rounded-xl bg-gold/10 border border-gold/20 flex items-center justify-center mb-4">
                    <svg class="w-6 h-6 text-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z" />
                    </svg>
                  </div>
                  <h3 class="font-display text-lg text-white font-bold mb-2">Intimate Class Size</h3>
                  <p class="text-slate text-sm leading-relaxed">
                    60 students selected for the inaugural batch. An exceptionally low
                    student-to-practitioner ratio that won't scale this small again.
                  </p>
                </div>

                <div>
                  <div class="w-12 h-12 rounded-xl bg-gold/10 border border-gold/20 flex items-center justify-center mb-4">
                    <svg class="w-6 h-6 text-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                    </svg>
                  </div>
                  <h3 class="font-display text-lg text-white font-bold mb-2">Direct Faculty Access</h3>
                  <p class="text-slate text-sm leading-relaxed">
                    Founding cohort members get unparalleled access to practitioners and
                    leadership — the kind of access that becomes impossible at scale.
                  </p>
                </div>

                <div>
                  <div class="w-12 h-12 rounded-xl bg-gold/10 border border-gold/20 flex items-center justify-center mb-4">
                    <svg class="w-6 h-6 text-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                    </svg>
                  </div>
                  <h3 class="font-display text-lg text-white font-bold mb-2">Legacy Status</h3>
                  <p class="text-slate text-sm leading-relaxed">
                    The founding cohort defines the culture, the standards, and the network.
                    As alumni, they carry permanent founding-member distinction.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-24 md:py-32 bg-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8 text-center">
        <h2 class="font-display text-3xl md:text-4xl text-navy font-bold mb-6">
          Interested in the Founding Cohort?
        </h2>
        <p class="text-lg text-charcoal/70 mb-10 max-w-2xl mx-auto">
          Applications for the June 2027 cohort will open soon. Express your interest
          now to receive priority access and early updates.
        </p>
        <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
          <RouterLink
            to="/admissions"
            class="inline-flex items-center gap-3 bg-gold hover:bg-gold-dark text-navy font-semibold px-8 py-4 rounded-lg transition-colors text-lg"
          >
            Express Your Interest
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
            </svg>
          </RouterLink>
          <RouterLink
            to="/why-us"
            class="inline-flex items-center gap-2 text-navy/70 hover:text-navy font-medium px-6 py-4 transition-colors"
          >
            Why Aureum?
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </RouterLink>
        </div>
      </div>
    </section>
  </div>
</template>
