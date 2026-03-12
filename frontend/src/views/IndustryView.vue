<script setup lang="ts">
import { RouterLink } from 'vue-router'

const participationCategories = [
  {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M12 21v-8.25M15.75 21v-8.25M8.25 21v-8.25M3 9l9-6 9 6m-1.5 12V10.332A48.36 48.36 0 0 0 12 9.75c-2.551 0-5.056.2-7.5.582V21" /></svg>`,
    title: 'Advisory Council',
    description:
      'A governing body of senior finance leaders who shape curriculum direction, validate learning outcomes, and ensure the program stays ahead of industry shifts.',
  },
  {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.438 60.438 0 0 0-.491 6.347A48.62 48.62 0 0 1 12 20.904a48.62 48.62 0 0 1 8.232-4.41 60.46 60.46 0 0 0-.491-6.347m-15.482 0a50.636 50.636 0 0 0-2.658-.813A59.906 59.906 0 0 1 12 3.493a59.903 59.903 0 0 1 10.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.717 50.717 0 0 1 12 13.489a50.702 50.702 0 0 1 7.74-3.342M6.75 15a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm0 0v-3.675A55.378 55.378 0 0 1 12 8.443m-7.007 11.55A5.981 5.981 0 0 0 6.75 15.75v-1.5" /></svg>`,
    title: 'Practitioner Faculty',
    description:
      'CXOs and senior practitioners who teach core modules from firsthand experience — bringing current deal flow, market perspective, and institutional knowledge into every session.',
  },
  {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 0 1-.825-.242m9.345-8.334a2.126 2.126 0 0 0-.476-.095 48.64 48.64 0 0 0-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0 0 11.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155" /></svg>`,
    title: 'Industry Mentors',
    description:
      'One-on-one mentorship pairing students with experienced finance professionals who guide career strategy, sharpen thinking, and open doors across the industry.',
  },
  {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M20.25 14.15v4.25c0 1.094-.787 2.036-1.872 2.18-2.087.277-4.216.42-6.378.42s-4.291-.143-6.378-.42c-1.085-.144-1.872-1.086-1.872-2.18v-4.25m16.5 0a2.18 2.18 0 0 0 .75-1.661V8.706c0-1.081-.768-2.015-1.837-2.175a48.114 48.114 0 0 0-3.413-.387m4.5 8.006c-.194.165-.42.295-.673.38A23.978 23.978 0 0 1 12 15.75c-2.648 0-5.195-.429-7.577-1.22a2.016 2.016 0 0 1-.673-.38m0 0A2.18 2.18 0 0 1 3 12.489V8.706c0-1.081.768-2.015 1.837-2.175a48.111 48.111 0 0 1 3.413-.387m7.5 0V5.25A2.25 2.25 0 0 0 13.5 3h-3a2.25 2.25 0 0 0-2.25 2.25v.894m7.5 0a48.667 48.667 0 0 0-7.5 0" /></svg>`,
    title: 'Hiring Partners',
    description:
      'Leading financial institutions committed to recruiting Aureum graduates — participating in capstone evaluations, conducting masterclasses, and offering placement pathways.',
  },
]

const leaders = [
  { name: 'Rajesh Mehta', title: 'Managing Director', company: 'Goldman Sachs India', initials: 'RM', color: 'bg-gold-dark', logo: 'https://logo.clearbit.com/goldmansachs.com', quote: 'Aureum is building what the industry has needed for decades.' },
  { name: 'Priya Sharma', title: 'Chief Investment Officer', company: 'HDFC AMC', initials: 'PS', color: 'bg-navy-light', logo: 'https://logo.clearbit.com/hdfcfund.com', quote: 'The practitioner-first model produces genuinely prepared professionals.' },
  { name: 'Vikram Iyer', title: 'Chief Executive Officer', company: 'Axis Capital', initials: 'VI', color: 'bg-charcoal', logo: 'https://logo.clearbit.com/axisbank.com', quote: 'I teach here because the students match the intensity of my teams.' },
  { name: 'Ananya Desai', title: 'Partner', company: 'McKinsey & Company', initials: 'AD', color: 'bg-gold-dark', logo: 'https://logo.clearbit.com/mckinsey.com', quote: 'The case pod format mirrors how real advisory engagements work.' },
  { name: 'Sanjay Nair', title: 'Head of Investment Banking', company: 'JP Morgan India', initials: 'SN', color: 'bg-navy-light', logo: 'https://logo.clearbit.com/jpmorgan.com', quote: 'Aureum graduates arrive with institutional-grade analytical rigor.' },
  { name: 'Meera Krishnan', title: 'Chief Financial Officer', company: 'Bajaj Finserv', initials: 'MK', color: 'bg-charcoal', logo: 'https://logo.clearbit.com/bajajfinserv.in', quote: 'This is the closest thing to on-the-job training outside of a desk.' },
  { name: 'Arjun Reddy', title: 'Managing Director', company: 'Kotak Investment Banking', initials: 'AR', color: 'bg-gold-dark', logo: 'https://logo.clearbit.com/kotak.com', quote: 'The capstone projects have directly informed our strategic thinking.' },
  { name: 'Kavita Patel', title: 'Vice President', company: 'ICICI Securities', initials: 'KP', color: 'bg-navy-light', logo: 'https://logo.clearbit.com/icicisecurities.com', quote: 'Mentoring Aureum students is among the most rewarding work I do.' },
]

const projectTypes = [
  {
    title: 'M&A Due Diligence',
    description:
      'Students conduct comprehensive due diligence on live acquisition targets — analyzing financials, assessing synergies, and presenting findings to senior deal teams.',
    tag: 'Investment Banking',
  },
  {
    title: 'Portfolio Risk Assessment',
    description:
      'Teams model and stress-test portfolio risk under multiple macroeconomic scenarios, delivering institutional-grade reports to asset management partners.',
    tag: 'Asset Management',
  },
  {
    title: 'Fintech Product Strategy',
    description:
      'Cross-functional pods design go-to-market strategies for emerging fintech products — from market sizing and competitive analysis to regulatory mapping.',
    tag: 'Financial Technology',
  },
]
</script>

<template>
  <div>
    <!-- Hero -->
    <section class="relative bg-navy pt-32 pb-20 lg:pb-28 overflow-hidden">
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_bottom_left,_var(--color-navy-light)_0%,_transparent_60%)]" />
      <div class="relative max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl">
          <p class="text-gold text-sm font-semibold tracking-[0.2em] uppercase mb-6">
            Industry
          </p>
          <h1 class="font-display text-4xl md:text-5xl lg:text-6xl text-white font-bold leading-tight mb-6">
            Built With the Industry.<br />
            Not Just For It.
          </h1>
          <p class="text-lg md:text-xl text-slate leading-relaxed max-w-2xl">
            Over 50 senior finance leaders co-create the Aureum learning
            experience — teaching modules, mentoring students, sourcing projects,
            and hiring graduates. This is not an advisory board on paper. It is
            a living partnership.
          </p>
        </div>
      </div>
    </section>

    <!-- How Industry Participates -->
    <section class="py-20 lg:py-28 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mb-16">
          <p class="text-gold text-sm font-semibold tracking-[0.2em] uppercase mb-4">
            How Industry Participates
          </p>
          <h2 class="font-display text-3xl md:text-4xl text-charcoal font-bold mb-6">
            Four layers of engagement
          </h2>
          <p class="text-slate text-lg leading-relaxed">
            Industry involvement at Aureum is not tokenistic. Leaders participate
            at every level — from shaping strategy to evaluating graduates.
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-6 lg:gap-8">
          <div
            v-for="category in participationCategories"
            :key="category.title"
            class="bg-white rounded-xl p-8 lg:p-10 border border-charcoal/5 transition-all duration-300 hover:shadow-lg hover:shadow-gold/5"
          >
            <div class="w-14 h-14 rounded-xl bg-gold/10 flex items-center justify-center text-gold mb-6" v-html="category.icon" />
            <h3 class="font-display text-xl lg:text-2xl text-charcoal font-bold mb-3">
              {{ category.title }}
            </h3>
            <p class="text-slate leading-relaxed">
              {{ category.description }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Leaders -->
    <section class="py-20 lg:py-28 bg-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mb-16">
          <p class="text-gold text-sm font-semibold tracking-[0.2em] uppercase mb-4">
            Featured Leaders
          </p>
          <h2 class="font-display text-3xl md:text-4xl text-charcoal font-bold mb-6">
            The people shaping Aureum
          </h2>
          <p class="text-slate text-lg leading-relaxed">
            Our network includes managing directors, chief investment officers,
            and partners from India's most respected financial institutions.
          </p>
        </div>

        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div
            v-for="leader in leaders"
            :key="leader.name"
            class="group bg-off-white rounded-xl p-6 border border-charcoal/5 transition-all duration-300 hover:shadow-lg hover:shadow-gold/5 hover:border-gold/20"
          >
            <!-- Avatar & Company Logo -->
            <div class="flex items-center gap-3 mb-5">
              <div
                class="w-14 h-14 rounded-full flex items-center justify-center text-white font-display font-bold text-lg shrink-0"
                :class="leader.color"
              >
                {{ leader.initials }}
              </div>
              <div class="w-10 h-10 rounded-lg bg-white border border-charcoal/10 flex items-center justify-center p-1.5 shrink-0">
                <img
                  :src="leader.logo"
                  :alt="leader.company + ' logo'"
                  class="w-full h-full object-contain"
                  loading="lazy"
                />
              </div>
            </div>
            <h3 class="font-display text-lg text-charcoal font-bold leading-snug">
              {{ leader.name }}
            </h3>
            <p class="text-sm text-gold-dark font-medium mt-1">
              {{ leader.title }}
            </p>
            <p class="text-sm text-slate mt-0.5 mb-4">
              {{ leader.company }}
            </p>
            <p class="text-sm text-slate/80 italic leading-relaxed border-t border-charcoal/5 pt-4">
              "{{ leader.quote }}"
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Industry Projects -->
    <section class="py-20 lg:py-28 bg-navy">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mb-16">
          <p class="text-gold text-sm font-semibold tracking-[0.2em] uppercase mb-4">
            Industry Projects
          </p>
          <h2 class="font-display text-3xl md:text-4xl text-white font-bold mb-6">
            Real problems. Real stakes.
          </h2>
          <p class="text-slate text-lg leading-relaxed">
            Partner companies bring live strategic challenges to Aureum. Students
            work in structured pods to deliver actionable analysis — building a
            portfolio of institutional-grade work before they graduate.
          </p>
        </div>

        <div class="grid lg:grid-cols-3 gap-6 lg:gap-8">
          <div
            v-for="project in projectTypes"
            :key="project.title"
            class="bg-white/[0.04] backdrop-blur-sm rounded-xl p-8 border border-white/10 transition-all duration-300 hover:border-gold/30 hover:bg-white/[0.07]"
          >
            <span class="inline-block text-xs font-semibold text-gold bg-gold/10 px-3 py-1 rounded-full mb-5">
              {{ project.tag }}
            </span>
            <h3 class="font-display text-xl text-white font-bold mb-3">
              {{ project.title }}
            </h3>
            <p class="text-slate leading-relaxed text-sm">
              {{ project.description }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- For Industry Leaders CTA -->
    <section class="py-20 lg:py-28 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-4xl mx-auto text-center">
          <p class="text-gold text-sm font-semibold tracking-[0.2em] uppercase mb-4">
            For Industry Leaders
          </p>
          <h2 class="font-display text-3xl md:text-4xl text-charcoal font-bold mb-6">
            Shape the Next Generation<br />of Finance Leaders
          </h2>
          <p class="text-slate text-lg leading-relaxed max-w-2xl mx-auto mb-10">
            Join a growing network of senior professionals who are redefining
            finance education. Whether as faculty, mentors, or project partners,
            your expertise directly shapes the industry's future talent pipeline.
          </p>
          <RouterLink
            to="/contact#industry"
            class="inline-flex items-center gap-2 bg-gold hover:bg-gold-dark text-navy font-semibold px-8 py-4 rounded transition-colors text-lg"
          >
            Get Involved
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
            </svg>
          </RouterLink>
        </div>
      </div>
    </section>
  </div>
</template>
