<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { onMounted, onUnmounted, ref } from 'vue'

const observedElements = ref<IntersectionObserver | null>(null)

onMounted(() => {
  observedElements.value = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible')
        }
      })
    },
    { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
  )

  document.querySelectorAll('.fade-up').forEach((el) => {
    observedElements.value?.observe(el)
  })
})

onUnmounted(() => {
  observedElements.value?.disconnect()
})

const companies = [
  'Goldman Sachs',
  'JP Morgan',
  'HDFC',
  'ICICI',
  'Kotak',
  'Axis',
  'Aditya Birla',
  'Bajaj Finserv',
]

const differentiators = [
  {
    title: 'Practitioner-Led Teaching',
    description:
      'Every class is taught by professionals who have operated at the highest levels of finance, not career academics.',
  },
  {
    title: 'Industry Co-Created Curriculum',
    description:
      'Our syllabus is designed in partnership with leading financial institutions to reflect what the market actually demands.',
  },
  {
    title: 'Real-World Immersive Projects',
    description:
      'Students work on live deals, real portfolios, and actual client briefs from day one of the program.',
  },
  {
    title: 'Day-1 Career Readiness',
    description:
      'Graduates enter the workforce fully equipped to perform, not needing months of on-the-job training.',
  },
]

const problems = [
  {
    number: '01',
    title: 'Generic Curriculum',
    description:
      'Traditional MBAs serve a buffet of everything but mastery of nothing. Finance is treated as a footnote, not a discipline.',
  },
  {
    number: '02',
    title: 'Theory-Heavy Instruction',
    description:
      'Case studies from decades past and textbook models that ignore the speed and complexity of modern markets.',
  },
  {
    number: '03',
    title: 'Long Ramp-Up to Productivity',
    description:
      'Employers spend months retraining MBA graduates. The gap between campus and desk has never been wider.',
  },
]
</script>

<template>
  <!-- ============================================ -->
  <!-- HERO -->
  <!-- ============================================ -->
  <section class="relative min-h-screen flex items-center justify-center bg-navy overflow-hidden">
    <!-- Animated gradient overlay -->
    <div class="hero-gradient absolute inset-0 opacity-30" aria-hidden="true"></div>
    <!-- Subtle grid pattern -->
    <div
      class="absolute inset-0 opacity-[0.03]"
      aria-hidden="true"
      style="background-image: linear-gradient(rgba(200,168,78,0.4) 1px, transparent 1px), linear-gradient(90deg, rgba(200,168,78,0.4) 1px, transparent 1px); background-size: 60px 60px"
    ></div>

    <div class="relative z-10 mx-auto max-w-5xl px-6 text-center">
      <h1
        class="font-display text-5xl leading-tight tracking-tight text-off-white sm:text-6xl md:text-7xl lg:text-8xl hero-title"
      >
        Where Finance<br />
        Meets <span class="text-gold">Mastery</span>
      </h1>
      <p
        class="mx-auto mt-8 max-w-2xl text-lg leading-relaxed text-slate sm:text-xl hero-subtitle"
      >
        A post-graduate institution built entirely by industry practitioners.
        Designed for those who want to lead in finance, not just study it.
      </p>
      <div class="mt-12 flex flex-col items-center gap-4 sm:flex-row sm:justify-center hero-ctas">
        <RouterLink
          to="/program"
          class="inline-flex items-center rounded-sm bg-gold px-8 py-4 text-sm font-semibold uppercase tracking-widest text-navy transition-all duration-300 hover:bg-gold-light hover:shadow-lg hover:shadow-gold/20"
        >
          Explore the Program
        </RouterLink>
        <RouterLink
          to="/contact#industry"
          class="inline-flex items-center rounded-sm border border-off-white/20 px-8 py-4 text-sm font-semibold uppercase tracking-widest text-off-white transition-all duration-300 hover:border-gold hover:text-gold"
        >
          For Industry Leaders
        </RouterLink>
      </div>
    </div>

    <!-- Scroll indicator -->
    <div class="absolute bottom-10 left-1/2 -translate-x-1/2 animate-bounce">
      <div class="h-10 w-[1px] bg-gradient-to-b from-transparent to-gold/40"></div>
    </div>
  </section>

  <!-- ============================================ -->
  <!-- WHY SECTION -->
  <!-- ============================================ -->
  <section class="bg-cream py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6">
      <div class="fade-up mx-auto max-w-3xl text-center">
        <h2 class="font-display text-3xl leading-snug tracking-tight text-navy sm:text-4xl md:text-5xl">
          Why a new kind of<br />finance institution?
        </h2>
        <p class="mt-6 text-lg leading-relaxed text-charcoal/70">
          The best minds in finance deserve better than what exists today.
        </p>
      </div>

      <div class="mt-16 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
        <div
          v-for="problem in problems"
          :key="problem.number"
          class="fade-up group rounded-lg border border-navy/5 bg-white p-8 transition-all duration-300 hover:border-gold/20 hover:shadow-xl hover:shadow-gold/5 sm:p-10"
        >
          <span
            class="font-display text-5xl font-bold text-gold/20 transition-colors duration-300 group-hover:text-gold/40"
          >
            {{ problem.number }}
          </span>
          <h3 class="mt-4 font-display text-xl font-semibold text-navy sm:text-2xl">
            {{ problem.title }}
          </h3>
          <p class="mt-3 text-base leading-relaxed text-charcoal/60">
            {{ problem.description }}
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================ -->
  <!-- DIFFERENTIATORS -->
  <!-- ============================================ -->
  <section class="bg-off-white py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6">
      <div class="fade-up">
        <h2 class="font-display text-3xl leading-snug tracking-tight text-navy sm:text-4xl md:text-5xl">
          Built Different.<br /><span class="text-gold">By Design.</span>
        </h2>
        <p class="mt-4 max-w-xl text-lg text-charcoal/60">
          Every element of Aureum is intentionally constructed to close the gap
          between learning and doing.
        </p>
      </div>

      <div class="mt-16 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <div
          v-for="(item, index) in differentiators"
          :key="item.title"
          class="fade-up group rounded-lg bg-navy p-8 transition-all duration-300 hover:bg-navy-light sm:p-10"
          :style="{ transitionDelay: `${index * 80}ms` }"
        >
          <div class="mb-6 h-[2px] w-8 bg-gold transition-all duration-300 group-hover:w-12"></div>
          <h3 class="font-display text-lg font-semibold leading-snug text-off-white sm:text-xl">
            {{ item.title }}
          </h3>
          <p class="mt-3 text-sm leading-relaxed text-slate">
            {{ item.description }}
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================ -->
  <!-- INDUSTRY PROOF -->
  <!-- ============================================ -->
  <section class="bg-cream py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6">
      <div class="fade-up mx-auto max-w-3xl text-center">
        <p class="text-xs font-semibold uppercase tracking-[0.25em] text-gold">
          Trusted Partnerships
        </p>
        <h2 class="mt-4 font-display text-3xl leading-snug tracking-tight text-navy sm:text-4xl md:text-5xl">
          Co-Created with India's<br />Finance Leaders
        </h2>
      </div>

      <!-- Company Logo Grid -->
      <div class="fade-up mt-16 grid grid-cols-2 gap-px overflow-hidden rounded-lg border border-navy/5 bg-navy/5 sm:grid-cols-4">
        <div
          v-for="company in companies"
          :key="company"
          class="flex h-24 items-center justify-center bg-white px-6 transition-colors duration-300 hover:bg-off-white sm:h-28"
        >
          <span class="text-sm font-semibold tracking-wide text-navy/30 sm:text-base">
            {{ company }}
          </span>
        </div>
      </div>

      <!-- Quote Block -->
      <div class="fade-up mx-auto mt-20 max-w-3xl text-center">
        <div class="relative">
          <svg
            class="mx-auto mb-6 h-8 w-8 text-gold/30"
            fill="currentColor"
            viewBox="0 0 32 32"
            aria-hidden="true"
          >
            <path d="M9.352 4C4.456 7.456 1 13.12 1 19.36c0 5.088 3.072 8.064 6.624 8.064 3.36 0 5.856-2.688 5.856-5.856 0-3.168-2.208-5.472-5.088-5.472-.576 0-1.344.096-1.536.192.48-3.264 3.552-7.104 6.624-9.024L9.352 4zm16.512 0c-4.8 3.456-8.256 9.12-8.256 15.36 0 5.088 3.072 8.064 6.624 8.064 3.264 0 5.856-2.688 5.856-5.856 0-3.168-2.304-5.472-5.184-5.472-.576 0-1.248.096-1.44.192.48-3.264 3.456-7.104 6.528-9.024L25.864 4z" />
          </svg>
          <blockquote class="font-display text-xl leading-relaxed text-navy/80 italic sm:text-2xl">
            The finance industry doesn't need more generalists. It needs professionals
            who can operate from day one.
          </blockquote>
          <div class="mt-6">
            <p class="text-sm font-semibold text-navy">Industry Advisory Council</p>
            <p class="text-sm text-charcoal/50">Aureum School of Finance</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================ -->
  <!-- PROGRAM OVERVIEW STRIP -->
  <!-- ============================================ -->
  <section class="bg-navy py-20 sm:py-24">
    <div class="mx-auto max-w-7xl px-6">
      <div class="fade-up flex flex-col items-center gap-10 lg:flex-row lg:justify-between">
        <!-- Info -->
        <div class="text-center lg:text-left">
          <p class="text-xs font-semibold uppercase tracking-[0.25em] text-gold">
            Flagship Program
          </p>
          <h2 class="mt-3 font-display text-2xl leading-snug text-off-white sm:text-3xl">
            Post Graduate Program in Finance
          </h2>
          <p class="mt-2 text-base text-slate">Commencing June 2027</p>
        </div>

        <!-- Stats -->
        <div class="flex flex-wrap justify-center gap-10 lg:gap-16">
          <div class="text-center">
            <p class="font-display text-3xl font-bold text-gold sm:text-4xl">12</p>
            <p class="mt-1 text-xs font-semibold uppercase tracking-widest text-slate">Months</p>
          </div>
          <div class="text-center">
            <p class="font-display text-3xl font-bold text-gold sm:text-4xl">100%</p>
            <p class="mt-1 text-xs font-semibold uppercase tracking-widest text-slate">Industry-Led</p>
          </div>
          <div class="text-center">
            <p class="font-display text-3xl font-bold text-gold sm:text-4xl">Mumbai</p>
            <p class="mt-1 text-xs font-semibold uppercase tracking-widest text-slate">Location</p>
          </div>
        </div>

        <!-- CTA -->
        <div class="shrink-0">
          <RouterLink
            to="/program"
            class="inline-flex items-center gap-2 rounded-sm border border-gold px-8 py-4 text-sm font-semibold uppercase tracking-widest text-gold transition-all duration-300 hover:bg-gold hover:text-navy"
          >
            Learn More
            <svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          </RouterLink>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================ -->
  <!-- FOUNDING COHORT CTA -->
  <!-- ============================================ -->
  <section class="relative overflow-hidden bg-charcoal py-24 sm:py-32">
    <!-- Decorative element -->
    <div
      class="absolute -right-40 -top-40 h-[500px] w-[500px] rounded-full bg-gold/[0.03] blur-3xl"
      aria-hidden="true"
    ></div>
    <div
      class="absolute -bottom-40 -left-40 h-[400px] w-[400px] rounded-full bg-gold/[0.02] blur-3xl"
      aria-hidden="true"
    ></div>

    <div class="relative z-10 mx-auto max-w-4xl px-6 text-center">
      <div class="fade-up">
        <p class="text-xs font-semibold uppercase tracking-[0.25em] text-gold">
          Limited Seats Available
        </p>
        <h2 class="mt-6 font-display text-4xl leading-tight tracking-tight text-off-white sm:text-5xl md:text-6xl">
          Join the Founding Cohort
        </h2>
        <p class="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-slate">
          Be part of the first class to graduate from India's only finance
          institution built entirely by the industry. The founding cohort will
          shape the legacy of Aureum for generations to come.
        </p>
        <div class="mt-10">
          <RouterLink
            to="/admissions"
            class="inline-flex items-center rounded-sm bg-gold px-10 py-4 text-sm font-semibold uppercase tracking-widest text-navy transition-all duration-300 hover:bg-gold-light hover:shadow-lg hover:shadow-gold/20"
          >
            Apply Now
          </RouterLink>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================ -->
  <!-- STAY CONNECTED MICRO-SECTION -->
  <!-- ============================================ -->
  <section class="bg-off-white py-12 sm:py-16">
    <div class="mx-auto max-w-7xl px-6 text-center">
      <p class="text-base text-charcoal/60">
        Want to stay updated?
        <RouterLink
          to="/contact"
          class="font-semibold text-navy underline decoration-gold/40 underline-offset-4 transition-colors duration-200 hover:text-gold"
        >
          Stay Connected
        </RouterLink>
      </p>
    </div>
  </section>
</template>

<style scoped>
/* ---- Hero Animations ---- */
.hero-gradient {
  background: radial-gradient(
      ellipse 80% 50% at 50% 0%,
      rgba(200, 168, 78, 0.08),
      transparent
    ),
    radial-gradient(
      ellipse 60% 60% at 80% 100%,
      rgba(22, 32, 64, 0.6),
      transparent
    );
  animation: gradient-shift 12s ease-in-out infinite alternate;
}

@keyframes gradient-shift {
  0% {
    opacity: 0.2;
    transform: scale(1) translateY(0);
  }
  100% {
    opacity: 0.35;
    transform: scale(1.05) translateY(-20px);
  }
}

.hero-title {
  opacity: 0;
  transform: translateY(30px);
  animation: hero-reveal 1s cubic-bezier(0.22, 1, 0.36, 1) 0.2s forwards;
}

.hero-subtitle {
  opacity: 0;
  transform: translateY(20px);
  animation: hero-reveal 1s cubic-bezier(0.22, 1, 0.36, 1) 0.5s forwards;
}

.hero-ctas {
  opacity: 0;
  transform: translateY(20px);
  animation: hero-reveal 1s cubic-bezier(0.22, 1, 0.36, 1) 0.8s forwards;
}

@keyframes hero-reveal {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* ---- Scroll-triggered fade-up ---- */
.fade-up {
  opacity: 0;
  transform: translateY(32px);
  transition: opacity 0.7s cubic-bezier(0.22, 1, 0.36, 1),
    transform 0.7s cubic-bezier(0.22, 1, 0.36, 1);
}

.fade-up.is-visible {
  opacity: 1;
  transform: translateY(0);
}
</style>
