<script setup lang="ts">
import { ref, reactive } from 'vue'
import { RouterLink } from 'vue-router'
import { submitStudentLead } from '@/lib/api'

/* ── FAQ Accordion ── */
const faqs = [
  {
    question: 'Is Aureum accredited?',
    answer:
      'Aureum School of Finance is currently in the process of securing accreditation from the relevant regulatory bodies. As a new institution, we are committed to meeting and exceeding every standard. Our founding cohort will benefit from the programme well before formal accreditation timelines, and we are transparent about our progress at every stage.',
  },
  {
    question: 'What makes this different from a traditional MBA?',
    answer:
      'Unlike a generalist MBA, Aureum is built exclusively around finance. Every course, case study, and industry engagement is designed for students who want careers in banking, asset management, fintech, or corporate finance. Our faculty are practitioners, our curriculum is co-created with employers, and our learning model prioritises live deal experience over theoretical lectures.',
  },
  {
    question: 'Is work experience required?',
    answer:
      'No. We welcome exceptional candidates straight out of undergraduate programs as well as professionals with up to five years of experience. What matters most is intellectual curiosity, a genuine interest in finance, and the drive to do meaningful work.',
  },
  {
    question: 'What is the selection process?',
    answer:
      'The process has three stages: a written application with essays and academic records, followed by a structured interview with our admissions committee, and finally a brief case discussion to assess analytical thinking. We evaluate potential, not just credentials.',
  },
  {
    question: 'Are scholarships available?',
    answer:
      'Yes. The founding cohort will have access to special scholarship pricing, merit-based tuition reductions, and need-based financial aid. We are committed to ensuring that financial constraints do not prevent talented candidates from joining.',
  },
  {
    question: 'Where will the campus be?',
    answer:
      'Aureum will be based in Mumbai — India\'s financial capital. Our campus will be located with easy access to key financial districts, enabling seamless integration of classroom learning and industry exposure.',
  },
  {
    question: 'When do applications open?',
    answer:
      'Applications for the founding cohort (Class of 2028) open in October 2026. You can register your interest now to receive early updates, priority application access, and invitations to exclusive preview events.',
  },
]

const openFaq = ref<number | null>(null)
const toggleFaq = (index: number) => {
  openFaq.value = openFaq.value === index ? null : index
}

/* ── Founding Cohort Advantages ── */
const advantages = [
  {
    title: 'Shape the Legacy',
    description:
      'As a founding member, you help define institutional culture, traditions, and the values that will guide generations of Aureum graduates.',
    icon: 'M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.562.562 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.562.562 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z',
  },
  {
    title: 'Intimate Access',
    description:
      'A 60-student cohort means direct relationships with faculty, personalised mentorship, and a learning environment that adapts to you.',
    icon: 'M18 18.72a9.094 9.094 0 003.741-.479 3 3 0 00-4.682-2.72m.94 3.198l.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0112 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 016 18.719m12 0a5.971 5.971 0 00-.941-3.197m0 0A5.995 5.995 0 0012 12.75a5.995 5.995 0 00-5.058 2.772m0 0a3 3 0 00-4.681 2.72 8.986 8.986 0 003.74.477m.94-3.197a5.971 5.971 0 00-.94 3.197M15 6.75a3 3 0 11-6 0 3 3 0 016 0zm6 3a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0zm-13.5 0a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0z',
  },
  {
    title: 'Pioneer Advantage',
    description:
      'First graduates carry a unique distinction. The strongest alumni bonds, the closest industry relationships, and a story only founders can tell.',
    icon: 'M15.59 14.37a6 6 0 01-5.84 7.38v-4.8m5.84-2.58a14.98 14.98 0 006.16-12.12A14.98 14.98 0 009.631 8.41m5.96 5.96a14.926 14.926 0 01-5.841 2.58m-.119-8.54a6 6 0 00-7.381 5.84h4.8m2.581-5.84a14.927 14.927 0 00-2.58 5.84m2.699 2.7c-.103.021-.207.041-.311.06a15.09 15.09 0 01-2.448-2.448 14.9 14.9 0 01.06-.312m-2.24 2.39a4.493 4.493 0 00-1.757 4.306 4.493 4.493 0 004.306-1.758M16.5 9a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z',
  },
  {
    title: 'Special Pricing',
    description:
      'Founding cohort members receive preferential tuition, exclusive scholarship opportunities, and pricing that reflects our partnership in building something new.',
    icon: 'M2.25 18.75a60.07 60.07 0 0115.797 2.101c.727.198 1.453-.342 1.453-1.096V18.75M3.75 4.5v.75A.75.75 0 013 6h-.75m0 0v-.375c0-.621.504-1.125 1.125-1.125H20.25M2.25 6v9m18-10.5v.75c0 .414.336.75.75.75h.75m-1.5-1.5h.375c.621 0 1.125.504 1.125 1.125v9.75c0 .621-.504 1.125-1.125 1.125h-.375m1.5-1.5H21a.75.75 0 00-.75.75v.75m0 0H3.75m0 0h-.375a1.125 1.125 0 01-1.125-1.125V15m1.5 1.5v-.75A.75.75 0 003 15h-.75M15 10.5a3 3 0 11-6 0 3 3 0 016 0zm3 0h.008v.008H18V10.5zm-12 0h.008v.008H6V10.5z',
  },
]

/* ── Timeline ── */
const timeline = [
  { label: 'Interest Registration', date: 'Open Now', active: true },
  { label: 'Applications Open', date: 'October 2026', active: false },
  { label: 'Interview Rounds', date: 'Dec 2026 – Mar 2027', active: false },
  { label: 'Offers Released', date: 'April 2027', active: false },
  { label: 'Program Begins', date: 'June 2027', active: false },
]

/* ── Lead Form ── */
const formStatus = ref<'idle' | 'loading' | 'success' | 'error'>('idle')
const formError = ref('')

const form = reactive({
  full_name: '',
  email: '',
  phone: '',
  qualification: '',
  experience: '',
  area_of_interest: '',
  message: '',
})

const qualifications = ['B.Com', 'B.Tech', 'BBA', 'CA', 'CFA', 'Other']
const experienceLevels = ['0 – 1 years', '1 – 3 years', '3 – 5 years', '5+ years']

const handleSubmit = async () => {
  formStatus.value = 'loading'
  formError.value = ''
  try {
    await submitStudentLead({
      full_name: form.full_name,
      email: form.email,
      phone: form.phone,
      qualification: form.qualification,
      experience: form.experience,
      area_of_interest: form.area_of_interest,
      message: form.message,
    })
    formStatus.value = 'success'
    Object.assign(form, {
      full_name: '',
      email: '',
      phone: '',
      qualification: '',
      experience: '',
      area_of_interest: '',
      message: '',
    })
  } catch (err: any) {
    formStatus.value = 'error'
    formError.value =
      err?.response?.data?.detail ||
      'Something went wrong. Please try again later.'
  }
}
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
          <div
            class="inline-flex items-center gap-2 bg-gold/10 border border-gold/20 rounded-full px-4 py-1.5 mb-8"
          >
            <span class="w-2 h-2 rounded-full bg-gold animate-pulse" />
            <span class="text-gold text-xs font-semibold tracking-wide uppercase">
              Class of 2028 — Admissions Opening Soon
            </span>
          </div>
          <h1
            class="font-display text-4xl md:text-5xl lg:text-6xl font-bold text-white leading-tight mb-6"
          >
            The Founding
            <span class="text-gold">Cohort</span>
          </h1>
          <p class="text-white/60 text-lg lg:text-xl leading-relaxed max-w-2xl">
            An invitation to be among the first. The founding class of Aureum
            School of Finance will define what this institution becomes — and
            carry that distinction for life.
          </p>
        </div>
      </div>
    </section>

    <!-- Why the Founding Cohort -->
    <section class="py-20 lg:py-28 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mx-auto text-center mb-16">
          <p
            class="text-gold-dark uppercase tracking-[0.2em] text-xs font-semibold mb-4"
          >
            Why the Founding Cohort
          </p>
          <h2
            class="font-display text-3xl md:text-4xl font-bold text-charcoal mb-6"
          >
            Four Reasons to Be First
          </h2>
          <p class="text-slate text-lg leading-relaxed">
            Joining a founding class is rare. The advantages are structural,
            not just sentimental.
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-6">
          <div
            v-for="item in advantages"
            :key="item.title"
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
                  :d="item.icon"
                />
              </svg>
            </div>
            <h3 class="font-display text-xl font-semibold text-charcoal mb-3">
              {{ item.title }}
            </h3>
            <p class="text-slate text-sm leading-relaxed">
              {{ item.description }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Admissions Timeline -->
    <section class="py-20 lg:py-28 bg-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mx-auto text-center mb-16">
          <p
            class="text-gold-dark uppercase tracking-[0.2em] text-xs font-semibold mb-4"
          >
            Admissions Timeline
          </p>
          <h2
            class="font-display text-3xl md:text-4xl font-bold text-charcoal mb-6"
          >
            Key Dates
          </h2>
        </div>

        <div class="max-w-2xl mx-auto">
          <div class="relative">
            <!-- Vertical line -->
            <div
              class="absolute left-[19px] top-2 bottom-2 w-px bg-black/10"
            />

            <div
              v-for="(step, index) in timeline"
              :key="step.label"
              class="relative flex items-start gap-6 pb-10 last:pb-0"
            >
              <!-- Dot -->
              <div class="relative z-10 flex-shrink-0">
                <div
                  class="w-10 h-10 rounded-full flex items-center justify-center"
                  :class="
                    step.active
                      ? 'bg-gold text-navy'
                      : 'bg-white border-2 border-black/10 text-slate'
                  "
                >
                  <span class="text-xs font-bold">{{
                    String(index + 1).padStart(2, '0')
                  }}</span>
                </div>
              </div>

              <!-- Content -->
              <div class="pt-1.5">
                <h3
                  class="font-display text-lg font-semibold"
                  :class="step.active ? 'text-gold-dark' : 'text-charcoal'"
                >
                  {{ step.label }}
                </h3>
                <p class="text-slate text-sm mt-0.5 flex items-center gap-2">
                  {{ step.date }}
                  <span
                    v-if="step.active"
                    class="inline-flex items-center gap-1 bg-emerald-50 text-emerald-700 text-xs font-semibold px-2 py-0.5 rounded-full"
                  >
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-500" />
                    Live
                  </span>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Eligibility -->
    <section class="py-20 lg:py-28 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="grid lg:grid-cols-2 gap-16 items-center">
          <div>
            <p
              class="text-gold-dark uppercase tracking-[0.2em] text-xs font-semibold mb-4"
            >
              Eligibility
            </p>
            <h2
              class="font-display text-3xl md:text-4xl font-bold text-charcoal mb-6"
            >
              Who Should Apply
            </h2>
            <p class="text-slate text-lg leading-relaxed mb-8">
              Aureum is for ambitious individuals who see finance not just as a
              career, but as a craft worth mastering. We look for potential,
              intellectual honesty, and the willingness to work hard.
            </p>
            <ul class="space-y-4">
              <li class="flex items-start gap-3">
                <svg
                  class="w-5 h-5 text-gold-dark mt-0.5 flex-shrink-0"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M4.5 12.75l6 6 9-13.5"
                  />
                </svg>
                <span class="text-charcoal"
                  >Bachelor's degree in any discipline</span
                >
              </li>
              <li class="flex items-start gap-3">
                <svg
                  class="w-5 h-5 text-gold-dark mt-0.5 flex-shrink-0"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M4.5 12.75l6 6 9-13.5"
                  />
                </svg>
                <span class="text-charcoal"
                  >0 – 5 years of work experience (freshers welcome)</span
                >
              </li>
              <li class="flex items-start gap-3">
                <svg
                  class="w-5 h-5 text-gold-dark mt-0.5 flex-shrink-0"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M4.5 12.75l6 6 9-13.5"
                  />
                </svg>
                <span class="text-charcoal"
                  >Genuine interest in finance, markets, or fintech</span
                >
              </li>
              <li class="flex items-start gap-3">
                <svg
                  class="w-5 h-5 text-gold-dark mt-0.5 flex-shrink-0"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M4.5 12.75l6 6 9-13.5"
                  />
                </svg>
                <span class="text-charcoal"
                  >GMAT / CAT scores are welcome but not mandatory</span
                >
              </li>
            </ul>
          </div>
          <div
            class="bg-white rounded-xl p-8 lg:p-10 shadow-sm border border-black/5"
          >
            <p
              class="text-gold-dark uppercase tracking-[0.2em] text-xs font-semibold mb-2"
            >
              Selection Process
            </p>
            <h3
              class="font-display text-2xl font-bold text-charcoal mb-6"
            >
              Three Stages
            </h3>
            <div class="space-y-6">
              <div class="flex gap-4">
                <div
                  class="flex-shrink-0 w-8 h-8 rounded-full bg-gold/10 flex items-center justify-center"
                >
                  <span
                    class="text-gold-dark font-display font-bold text-sm"
                    >1</span
                  >
                </div>
                <div>
                  <h4 class="font-semibold text-charcoal">Application</h4>
                  <p class="text-slate text-sm">
                    Essays, academic records, and a statement of purpose.
                  </p>
                </div>
              </div>
              <div class="flex gap-4">
                <div
                  class="flex-shrink-0 w-8 h-8 rounded-full bg-gold/10 flex items-center justify-center"
                >
                  <span
                    class="text-gold-dark font-display font-bold text-sm"
                    >2</span
                  >
                </div>
                <div>
                  <h4 class="font-semibold text-charcoal">Interview</h4>
                  <p class="text-slate text-sm">
                    A structured conversation with the admissions committee.
                  </p>
                </div>
              </div>
              <div class="flex gap-4">
                <div
                  class="flex-shrink-0 w-8 h-8 rounded-full bg-gold/10 flex items-center justify-center"
                >
                  <span
                    class="text-gold-dark font-display font-bold text-sm"
                    >3</span
                  >
                </div>
                <div>
                  <h4 class="font-semibold text-charcoal">Case Discussion</h4>
                  <p class="text-slate text-sm">
                    A brief analytical exercise to evaluate problem-solving
                    approach.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Fee Structure -->
    <section class="py-20 lg:py-28 bg-navy">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mx-auto text-center">
          <p
            class="text-gold uppercase tracking-[0.2em] text-xs font-semibold mb-4"
          >
            Tuition
          </p>
          <h2
            class="font-display text-3xl md:text-4xl font-bold text-white mb-6"
          >
            Investment in Your Future
          </h2>
          <div
            class="bg-white/5 border border-white/10 rounded-xl p-8 lg:p-10 mt-10"
          >
            <p class="text-white/50 text-sm uppercase tracking-wider mb-2">
              Program Fee (Tentative)
            </p>
            <p class="font-display text-4xl lg:text-5xl font-bold text-gold mb-2">
              &#8377;18,00,000
            </p>
            <p class="text-white/40 text-sm mb-8">
              For the full two-year programme, inclusive of tuition and learning
              materials.
            </p>
            <div class="grid sm:grid-cols-3 gap-6 text-left">
              <div class="bg-white/5 rounded-lg p-5">
                <h4
                  class="text-white font-semibold text-sm mb-1"
                >
                  Founding Cohort Scholarships
                </h4>
                <p class="text-white/40 text-sm">
                  Merit and need-based scholarships available exclusively for
                  the first class.
                </p>
              </div>
              <div class="bg-white/5 rounded-lg p-5">
                <h4
                  class="text-white font-semibold text-sm mb-1"
                >
                  EMI Options
                </h4>
                <p class="text-white/40 text-sm">
                  Flexible instalment plans through partner financial
                  institutions. No-cost EMI available.
                </p>
              </div>
              <div class="bg-white/5 rounded-lg p-5">
                <h4
                  class="text-white font-semibold text-sm mb-1"
                >
                  Education Loans
                </h4>
                <p class="text-white/40 text-sm">
                  Assistance with loan applications and documentation through
                  banking partners.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQs -->
    <section id="faqs" class="py-20 lg:py-28 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl mx-auto">
          <div class="text-center mb-16">
            <p
              class="text-gold-dark uppercase tracking-[0.2em] text-xs font-semibold mb-4"
            >
              FAQs
            </p>
            <h2
              class="font-display text-3xl md:text-4xl font-bold text-charcoal"
            >
              Common Questions
            </h2>
          </div>

          <div class="space-y-3">
            <div
              v-for="(faq, index) in faqs"
              :key="index"
              class="bg-white rounded-xl border border-black/5 overflow-hidden"
            >
              <button
                class="w-full flex items-center justify-between px-6 py-5 text-left group"
                @click="toggleFaq(index)"
              >
                <span
                  class="font-display font-semibold text-charcoal group-hover:text-gold-dark transition-colors pr-4"
                >
                  {{ faq.question }}
                </span>
                <svg
                  class="w-5 h-5 text-slate flex-shrink-0 transition-transform duration-200"
                  :class="openFaq === index ? 'rotate-180' : ''"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M19.5 8.25l-7.5 7.5-7.5-7.5"
                  />
                </svg>
              </button>
              <Transition
                enter-active-class="transition-all duration-200 ease-out"
                enter-from-class="max-h-0 opacity-0"
                enter-to-class="max-h-96 opacity-100"
                leave-active-class="transition-all duration-150 ease-in"
                leave-from-class="max-h-96 opacity-100"
                leave-to-class="max-h-0 opacity-0"
              >
                <div v-if="openFaq === index" class="overflow-hidden">
                  <p class="px-6 pb-5 text-slate text-sm leading-relaxed">
                    {{ faq.answer }}
                  </p>
                </div>
              </Transition>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Interest Form -->
    <section class="py-20 lg:py-28 bg-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-2xl mx-auto">
          <div class="text-center mb-12">
            <p
              class="text-gold-dark uppercase tracking-[0.2em] text-xs font-semibold mb-4"
            >
              Register Interest
            </p>
            <h2
              class="font-display text-3xl md:text-4xl font-bold text-charcoal mb-4"
            >
              Take the First Step
            </h2>
            <p class="text-slate text-lg leading-relaxed">
              Register your interest to receive priority access when
              applications open, invitations to preview events, and updates on
              the founding cohort.
            </p>
          </div>

          <!-- Success State -->
          <div
            v-if="formStatus === 'success'"
            class="bg-emerald-50 border border-emerald-200 rounded-xl p-8 text-center"
          >
            <div
              class="w-14 h-14 rounded-full bg-emerald-100 flex items-center justify-center mx-auto mb-4"
            >
              <svg
                class="w-7 h-7 text-emerald-600"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M4.5 12.75l6 6 9-13.5"
                />
              </svg>
            </div>
            <h3 class="font-display text-xl font-semibold text-charcoal mb-2">
              Interest Registered
            </h3>
            <p class="text-slate text-sm">
              Thank you for your interest in Aureum. Our admissions team will
              be in touch with next steps.
            </p>
            <button
              class="mt-6 text-gold-dark font-semibold text-sm hover:underline"
              @click="formStatus = 'idle'"
            >
              Submit another response
            </button>
          </div>

          <!-- Form -->
          <form
            v-else
            class="bg-cream/50 border border-black/5 rounded-xl p-8 lg:p-10 space-y-6"
            @submit.prevent="handleSubmit"
          >
            <div class="grid sm:grid-cols-2 gap-6">
              <div>
                <label
                  class="block text-charcoal text-sm font-medium mb-1.5"
                  >Full Name <span class="text-red-400">*</span></label
                >
                <input
                  v-model="form.full_name"
                  type="text"
                  required
                  placeholder="Your full name"
                  class="w-full bg-white border border-black/10 rounded-lg px-4 py-3 text-sm text-charcoal placeholder-slate/50 focus:outline-none focus:border-gold/50 focus:ring-1 focus:ring-gold/20 transition"
                />
              </div>
              <div>
                <label
                  class="block text-charcoal text-sm font-medium mb-1.5"
                  >Email <span class="text-red-400">*</span></label
                >
                <input
                  v-model="form.email"
                  type="email"
                  required
                  placeholder="you@example.com"
                  class="w-full bg-white border border-black/10 rounded-lg px-4 py-3 text-sm text-charcoal placeholder-slate/50 focus:outline-none focus:border-gold/50 focus:ring-1 focus:ring-gold/20 transition"
                />
              </div>
            </div>

            <div class="grid sm:grid-cols-2 gap-6">
              <div>
                <label
                  class="block text-charcoal text-sm font-medium mb-1.5"
                  >Phone <span class="text-red-400">*</span></label
                >
                <input
                  v-model="form.phone"
                  type="tel"
                  required
                  placeholder="+91 98765 43210"
                  class="w-full bg-white border border-black/10 rounded-lg px-4 py-3 text-sm text-charcoal placeholder-slate/50 focus:outline-none focus:border-gold/50 focus:ring-1 focus:ring-gold/20 transition"
                />
              </div>
              <div>
                <label
                  class="block text-charcoal text-sm font-medium mb-1.5"
                  >Current Qualification
                  <span class="text-red-400">*</span></label
                >
                <select
                  v-model="form.qualification"
                  required
                  class="w-full bg-white border border-black/10 rounded-lg px-4 py-3 text-sm text-charcoal focus:outline-none focus:border-gold/50 focus:ring-1 focus:ring-gold/20 transition appearance-none"
                >
                  <option value="" disabled>Select qualification</option>
                  <option
                    v-for="q in qualifications"
                    :key="q"
                    :value="q"
                  >
                    {{ q }}
                  </option>
                </select>
              </div>
            </div>

            <div class="grid sm:grid-cols-2 gap-6">
              <div>
                <label
                  class="block text-charcoal text-sm font-medium mb-1.5"
                  >Years of Experience
                  <span class="text-red-400">*</span></label
                >
                <select
                  v-model="form.experience"
                  required
                  class="w-full bg-white border border-black/10 rounded-lg px-4 py-3 text-sm text-charcoal focus:outline-none focus:border-gold/50 focus:ring-1 focus:ring-gold/20 transition appearance-none"
                >
                  <option value="" disabled>Select experience</option>
                  <option
                    v-for="e in experienceLevels"
                    :key="e"
                    :value="e"
                  >
                    {{ e }}
                  </option>
                </select>
              </div>
              <div>
                <label
                  class="block text-charcoal text-sm font-medium mb-1.5"
                  >Area of Interest
                  <span class="text-red-400">*</span></label
                >
                <input
                  v-model="form.area_of_interest"
                  type="text"
                  required
                  placeholder="e.g. Investment Banking, Fintech"
                  class="w-full bg-white border border-black/10 rounded-lg px-4 py-3 text-sm text-charcoal placeholder-slate/50 focus:outline-none focus:border-gold/50 focus:ring-1 focus:ring-gold/20 transition"
                />
              </div>
            </div>

            <div>
              <label class="block text-charcoal text-sm font-medium mb-1.5"
                >Message
                <span class="text-slate/50 font-normal"
                  >(optional)</span
                ></label
              >
              <textarea
                v-model="form.message"
                rows="4"
                placeholder="Anything you'd like us to know..."
                class="w-full bg-white border border-black/10 rounded-lg px-4 py-3 text-sm text-charcoal placeholder-slate/50 focus:outline-none focus:border-gold/50 focus:ring-1 focus:ring-gold/20 transition resize-none"
              />
            </div>

            <!-- Error message -->
            <p
              v-if="formStatus === 'error'"
              class="text-red-500 text-sm"
            >
              {{ formError }}
            </p>

            <button
              type="submit"
              :disabled="formStatus === 'loading'"
              class="w-full bg-gold hover:bg-gold-dark text-navy font-semibold py-3.5 rounded-lg transition-colors text-sm disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {{
                formStatus === 'loading'
                  ? 'Submitting...'
                  : 'Register Interest'
              }}
            </button>

            <p class="text-slate/50 text-xs text-center">
              Your information is private and will only be used for admissions
              communications.
            </p>
          </form>
        </div>
      </div>
    </section>
  </div>
</template>
