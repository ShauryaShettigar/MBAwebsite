<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { ref, reactive, onMounted, onUnmounted } from 'vue'
import { submitStudentLead, submitIndustryLead, submitContactInquiry } from '@/lib/api'

// --- Tab state ---
const activeTab = ref<'student' | 'industry'>('student')

// Check if URL hash is #industry on mount
onMounted(() => {
  if (window.location.hash === '#industry') {
    activeTab.value = 'industry'
  }

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

const observedElements = ref<IntersectionObserver | null>(null)

onUnmounted(() => {
  observedElements.value?.disconnect()
})

// --- Student Form ---
const studentForm = reactive({
  fullName: '',
  email: '',
  phone: '',
  qualification: '',
  experience: '',
  interest: '',
  message: '',
})
const studentSubmitting = ref(false)
const studentSuccess = ref(false)
const studentError = ref('')

async function handleStudentSubmit() {
  studentError.value = ''
  if (!studentForm.fullName || !studentForm.email || !studentForm.phone || !studentForm.qualification || !studentForm.experience || !studentForm.interest) {
    studentError.value = 'Please fill in all required fields.'
    return
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(studentForm.email)) {
    studentError.value = 'Please enter a valid email address.'
    return
  }
  studentSubmitting.value = true
  try {
    await submitStudentLead({
      full_name: studentForm.fullName,
      email: studentForm.email,
      phone: studentForm.phone,
      qualification: studentForm.qualification,
      experience: studentForm.experience,
      area_of_interest: studentForm.interest,
      message: studentForm.message,
    })
    studentSuccess.value = true
    Object.assign(studentForm, { fullName: '', email: '', phone: '', qualification: '', experience: '', interest: '', message: '' })
  } catch {
    studentError.value = 'Something went wrong. Please try again later.'
  } finally {
    studentSubmitting.value = false
  }
}

// --- Industry Form ---
const industryForm = reactive({
  fullName: '',
  email: '',
  phone: '',
  designation: '',
  organization: '',
  engagement: '',
  message: '',
})
const industrySubmitting = ref(false)
const industrySuccess = ref(false)
const industryError = ref('')

async function handleIndustrySubmit() {
  industryError.value = ''
  if (!industryForm.fullName || !industryForm.email || !industryForm.phone || !industryForm.designation || !industryForm.organization || !industryForm.engagement) {
    industryError.value = 'Please fill in all required fields.'
    return
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(industryForm.email)) {
    industryError.value = 'Please enter a valid email address.'
    return
  }
  industrySubmitting.value = true
  try {
    await submitIndustryLead({
      full_name: industryForm.fullName,
      email: industryForm.email,
      phone: industryForm.phone,
      designation: industryForm.designation,
      organization: industryForm.organization,
      engagement_type: industryForm.engagement,
      message: industryForm.message,
    })
    industrySuccess.value = true
    Object.assign(industryForm, { fullName: '', email: '', phone: '', designation: '', organization: '', engagement: '', message: '' })
  } catch {
    industryError.value = 'Something went wrong. Please try again later.'
  } finally {
    industrySubmitting.value = false
  }
}

// --- General Contact Form ---
const contactForm = reactive({
  name: '',
  email: '',
  inquiryType: '',
  subject: '',
  message: '',
})
const contactSubmitting = ref(false)
const contactSuccess = ref(false)
const contactError = ref('')

async function handleContactSubmit() {
  contactError.value = ''
  if (!contactForm.name || !contactForm.email || !contactForm.inquiryType || !contactForm.subject || !contactForm.message) {
    contactError.value = 'Please fill in all required fields.'
    return
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(contactForm.email)) {
    contactError.value = 'Please enter a valid email address.'
    return
  }
  contactSubmitting.value = true
  try {
    await submitContactInquiry({
      name: contactForm.name,
      email: contactForm.email,
      inquiry_type: contactForm.inquiryType,
      subject: contactForm.subject,
      message: contactForm.message,
    })
    contactSuccess.value = true
    Object.assign(contactForm, { name: '', email: '', inquiryType: '', subject: '', message: '' })
  } catch {
    contactError.value = 'Something went wrong. Please try again later.'
  } finally {
    contactSubmitting.value = false
  }
}
</script>

<template>
  <div>
    <!-- ============================================ -->
    <!-- HERO -->
    <!-- ============================================ -->
    <section class="relative bg-navy pt-32 pb-24 md:pb-32 overflow-hidden">
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--color-navy-light)_0%,_transparent_60%)]" />
      <div class="absolute top-20 right-0 w-96 h-96 bg-gold/5 rounded-full blur-3xl" />

      <div class="relative max-w-7xl mx-auto px-6 lg:px-8">
        <div class="max-w-3xl">
          <div class="inline-flex items-center gap-2 mb-8">
            <span class="w-8 h-px bg-gold" />
            <span class="text-gold text-sm tracking-widest uppercase font-medium">Connect</span>
          </div>

          <h1 class="font-display text-4xl md:text-5xl lg:text-6xl text-white font-bold leading-tight mb-8">
            Get in <span class="text-gold">Touch</span>
          </h1>

          <p class="text-lg md:text-xl text-slate leading-relaxed max-w-2xl">
            Whether you're a prospective student or industry leader, we'd love to hear from you.
          </p>
        </div>
      </div>
    </section>

    <!-- ============================================ -->
    <!-- DUAL LEAD FORMS -->
    <!-- ============================================ -->
    <section class="py-20 md:py-28 bg-off-white">
      <div class="max-w-4xl mx-auto px-6 lg:px-8">
        <!-- Tab Switcher -->
        <div class="fade-up flex rounded-xl bg-navy/5 p-1.5 mb-12">
          <button
            @click="activeTab = 'student'"
            class="flex-1 py-4 px-6 rounded-lg text-sm font-semibold tracking-wide transition-all duration-300"
            :class="
              activeTab === 'student'
                ? 'bg-navy text-gold shadow-lg shadow-navy/20'
                : 'text-charcoal/50 hover:text-navy'
            "
          >
            I'm a Prospective Student
          </button>
          <button
            id="industry"
            @click="activeTab = 'industry'"
            class="flex-1 py-4 px-6 rounded-lg text-sm font-semibold tracking-wide transition-all duration-300"
            :class="
              activeTab === 'industry'
                ? 'bg-navy text-gold shadow-lg shadow-navy/20'
                : 'text-charcoal/50 hover:text-navy'
            "
          >
            I'm an Industry Leader
          </button>
        </div>

        <!-- ======== STUDENT FORM ======== -->
        <Transition name="form-fade" mode="out-in">
          <div v-if="activeTab === 'student'" key="student" class="fade-up">
            <!-- Success State -->
            <div v-if="studentSuccess" class="rounded-2xl bg-navy p-12 md:p-16 text-center">
              <div class="w-16 h-16 rounded-full bg-gold/15 flex items-center justify-center mx-auto mb-6">
                <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <h3 class="font-display text-2xl md:text-3xl text-white font-bold mb-4">Thank You for Your Interest</h3>
              <p class="text-slate text-lg max-w-lg mx-auto mb-8">
                We've received your enquiry. Our admissions team will be in touch within 48 hours.
              </p>
              <button
                @click="studentSuccess = false"
                class="text-gold font-semibold text-sm uppercase tracking-widest hover:text-gold-light transition-colors"
              >
                Submit Another Enquiry
              </button>
            </div>

            <!-- Form -->
            <form v-else @submit.prevent="handleStudentSubmit" class="rounded-2xl bg-navy p-8 md:p-12">
              <div class="mb-10">
                <h2 class="font-display text-2xl md:text-3xl text-white font-bold mb-3">
                  Register Your Interest
                </h2>
                <p class="text-slate">
                  Share your details and our admissions team will reach out to discuss next steps.
                </p>
              </div>

              <!-- Error -->
              <div v-if="studentError" class="mb-6 p-4 rounded-lg bg-red-500/10 border border-red-500/20">
                <p class="text-red-400 text-sm">{{ studentError }}</p>
              </div>

              <div class="grid gap-6 md:grid-cols-2">
                <!-- Full Name -->
                <div class="md:col-span-2">
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Full Name *</label>
                  <input
                    v-model="studentForm.fullName"
                    type="text"
                    required
                    placeholder="Enter your full name"
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30"
                  />
                </div>

                <!-- Email -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Email *</label>
                  <input
                    v-model="studentForm.email"
                    type="email"
                    required
                    placeholder="you@example.com"
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30"
                  />
                </div>

                <!-- Phone -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Phone *</label>
                  <input
                    v-model="studentForm.phone"
                    type="tel"
                    required
                    placeholder="+91 XXXXX XXXXX"
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30"
                  />
                </div>

                <!-- Current Qualification -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Current Qualification *</label>
                  <select
                    v-model="studentForm.qualification"
                    required
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30 appearance-none"
                  >
                    <option value="" disabled class="text-slate/50">Select qualification</option>
                    <option value="B.Com">B.Com</option>
                    <option value="B.Tech/B.E.">B.Tech/B.E.</option>
                    <option value="BBA/BMS">BBA/BMS</option>
                    <option value="CA/CFA">CA/CFA</option>
                    <option value="MBA">MBA</option>
                    <option value="Other">Other</option>
                  </select>
                </div>

                <!-- Years of Experience -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Years of Experience *</label>
                  <select
                    v-model="studentForm.experience"
                    required
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30 appearance-none"
                  >
                    <option value="" disabled class="text-slate/50">Select experience</option>
                    <option value="Fresher">Fresher</option>
                    <option value="1-2 years">1-2 years</option>
                    <option value="2-4 years">2-4 years</option>
                    <option value="4+ years">4+ years</option>
                  </select>
                </div>

                <!-- Area of Interest -->
                <div class="md:col-span-2">
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Area of Interest *</label>
                  <select
                    v-model="studentForm.interest"
                    required
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30 appearance-none"
                  >
                    <option value="" disabled class="text-slate/50">Select area of interest</option>
                    <option value="Investment Banking">Investment Banking</option>
                    <option value="Asset Management">Asset Management</option>
                    <option value="Private Equity">Private Equity</option>
                    <option value="Fintech">Fintech</option>
                    <option value="Corporate Finance">Corporate Finance</option>
                    <option value="Other">Other</option>
                  </select>
                </div>

                <!-- Message -->
                <div class="md:col-span-2">
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Message <span class="text-slate/40">(optional)</span></label>
                  <textarea
                    v-model="studentForm.message"
                    rows="4"
                    placeholder="Anything else you'd like us to know?"
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30 resize-none"
                  ></textarea>
                </div>
              </div>

              <div class="mt-8">
                <button
                  type="submit"
                  :disabled="studentSubmitting"
                  class="w-full sm:w-auto inline-flex items-center justify-center gap-2 rounded-lg bg-gold px-10 py-4 text-sm font-semibold uppercase tracking-widest text-navy transition-all duration-300 hover:bg-gold-light hover:shadow-lg hover:shadow-gold/20 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <svg v-if="studentSubmitting" class="animate-spin h-4 w-4" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                  </svg>
                  {{ studentSubmitting ? 'Submitting...' : 'Register Interest' }}
                </button>
              </div>
            </form>
          </div>

          <!-- ======== INDUSTRY FORM ======== -->
          <div v-else key="industry" class="fade-up">
            <!-- Success State -->
            <div v-if="industrySuccess" class="rounded-2xl bg-navy p-12 md:p-16 text-center">
              <div class="w-16 h-16 rounded-full bg-gold/15 flex items-center justify-center mx-auto mb-6">
                <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <h3 class="font-display text-2xl md:text-3xl text-white font-bold mb-4">Thank You for Your Interest</h3>
              <p class="text-slate text-lg max-w-lg mx-auto mb-8">
                We value your interest in shaping the next generation of finance leaders. Our partnerships team will be in touch shortly.
              </p>
              <button
                @click="industrySuccess = false"
                class="text-gold font-semibold text-sm uppercase tracking-widest hover:text-gold-light transition-colors"
              >
                Submit Another Enquiry
              </button>
            </div>

            <!-- Form -->
            <form v-else @submit.prevent="handleIndustrySubmit" class="rounded-2xl bg-navy p-8 md:p-12">
              <div class="mb-10">
                <h2 class="font-display text-2xl md:text-3xl text-white font-bold mb-3">
                  Express Your Interest
                </h2>
                <p class="text-slate">
                  Partner with Aureum to shape curriculum, mentor students, or recruit from India's most focused finance program.
                </p>
              </div>

              <!-- Error -->
              <div v-if="industryError" class="mb-6 p-4 rounded-lg bg-red-500/10 border border-red-500/20">
                <p class="text-red-400 text-sm">{{ industryError }}</p>
              </div>

              <div class="grid gap-6 md:grid-cols-2">
                <!-- Full Name -->
                <div class="md:col-span-2">
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Full Name *</label>
                  <input
                    v-model="industryForm.fullName"
                    type="text"
                    required
                    placeholder="Enter your full name"
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30"
                  />
                </div>

                <!-- Email -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Email *</label>
                  <input
                    v-model="industryForm.email"
                    type="email"
                    required
                    placeholder="you@company.com"
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30"
                  />
                </div>

                <!-- Phone -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Phone *</label>
                  <input
                    v-model="industryForm.phone"
                    type="tel"
                    required
                    placeholder="+91 XXXXX XXXXX"
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30"
                  />
                </div>

                <!-- Designation -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Designation *</label>
                  <input
                    v-model="industryForm.designation"
                    type="text"
                    required
                    placeholder="e.g. Managing Director"
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30"
                  />
                </div>

                <!-- Organization -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Organization *</label>
                  <input
                    v-model="industryForm.organization"
                    type="text"
                    required
                    placeholder="e.g. Goldman Sachs"
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30"
                  />
                </div>

                <!-- Engagement Type -->
                <div class="md:col-span-2">
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">How Would You Like to Engage? *</label>
                  <select
                    v-model="industryForm.engagement"
                    required
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30 appearance-none"
                  >
                    <option value="" disabled class="text-slate/50">Select engagement type</option>
                    <option value="Guest Faculty">Guest Faculty</option>
                    <option value="Mentor">Mentor</option>
                    <option value="Advisory Board">Advisory Board</option>
                    <option value="Hiring Partner">Hiring Partner</option>
                    <option value="Guest Speaker">Guest Speaker</option>
                    <option value="Other">Other</option>
                  </select>
                </div>

                <!-- Message -->
                <div class="md:col-span-2">
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Message <span class="text-slate/40">(optional)</span></label>
                  <textarea
                    v-model="industryForm.message"
                    rows="4"
                    placeholder="Tell us more about how you'd like to collaborate."
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30 resize-none"
                  ></textarea>
                </div>
              </div>

              <div class="mt-8">
                <button
                  type="submit"
                  :disabled="industrySubmitting"
                  class="w-full sm:w-auto inline-flex items-center justify-center gap-2 rounded-lg bg-gold px-10 py-4 text-sm font-semibold uppercase tracking-widest text-navy transition-all duration-300 hover:bg-gold-light hover:shadow-lg hover:shadow-gold/20 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <svg v-if="industrySubmitting" class="animate-spin h-4 w-4" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                  </svg>
                  {{ industrySubmitting ? 'Submitting...' : 'Express Interest' }}
                </button>
              </div>
            </form>
          </div>
        </Transition>
      </div>
    </section>

    <!-- ============================================ -->
    <!-- GENERAL CONTACT -->
    <!-- ============================================ -->
    <section class="py-20 md:py-28 bg-cream">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="grid lg:grid-cols-5 gap-16">
          <!-- Contact Info -->
          <div class="lg:col-span-2 fade-up">
            <span class="text-gold text-sm tracking-widest uppercase font-medium">General Enquiries</span>
            <h2 class="font-display text-3xl md:text-4xl text-navy font-bold mt-4 mb-8">
              Reach Us Directly
            </h2>

            <div class="space-y-8">
              <!-- Email -->
              <div class="flex items-start gap-4">
                <div class="w-10 h-10 rounded-lg bg-navy/5 flex items-center justify-center shrink-0">
                  <svg class="w-5 h-5 text-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs font-semibold uppercase tracking-widest text-charcoal/40 mb-1">Email</p>
                  <a href="mailto:admissions@aureum.edu" class="text-navy font-medium hover:text-gold transition-colors">
                    admissions@aureum.edu
                  </a>
                </div>
              </div>

              <!-- Phone -->
              <div class="flex items-start gap-4">
                <div class="w-10 h-10 rounded-lg bg-navy/5 flex items-center justify-center shrink-0">
                  <svg class="w-5 h-5 text-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs font-semibold uppercase tracking-widest text-charcoal/40 mb-1">Phone</p>
                  <p class="text-navy font-medium">+91 22 XXXX XXXX</p>
                </div>
              </div>

              <!-- Address -->
              <div class="flex items-start gap-4">
                <div class="w-10 h-10 rounded-lg bg-navy/5 flex items-center justify-center shrink-0">
                  <svg class="w-5 h-5 text-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs font-semibold uppercase tracking-widest text-charcoal/40 mb-1">Address</p>
                  <p class="text-navy font-medium">Mumbai, Maharashtra, India</p>
                </div>
              </div>
            </div>
          </div>

          <!-- General Contact Form -->
          <div class="lg:col-span-3 fade-up">
            <!-- Success State -->
            <div v-if="contactSuccess" class="rounded-2xl bg-navy p-12 text-center">
              <div class="w-16 h-16 rounded-full bg-gold/15 flex items-center justify-center mx-auto mb-6">
                <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <h3 class="font-display text-2xl text-white font-bold mb-4">Message Sent</h3>
              <p class="text-slate max-w-md mx-auto mb-8">
                Thank you for reaching out. We'll respond to your enquiry as soon as possible.
              </p>
              <button
                @click="contactSuccess = false"
                class="text-gold font-semibold text-sm uppercase tracking-widest hover:text-gold-light transition-colors"
              >
                Send Another Message
              </button>
            </div>

            <!-- Form -->
            <form v-else @submit.prevent="handleContactSubmit" class="rounded-2xl bg-navy p-8 md:p-10">
              <h3 class="font-display text-xl md:text-2xl text-white font-bold mb-8">
                Send Us a Message
              </h3>

              <!-- Error -->
              <div v-if="contactError" class="mb-6 p-4 rounded-lg bg-red-500/10 border border-red-500/20">
                <p class="text-red-400 text-sm">{{ contactError }}</p>
              </div>

              <div class="grid gap-6 md:grid-cols-2">
                <!-- Name -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Name *</label>
                  <input
                    v-model="contactForm.name"
                    type="text"
                    required
                    placeholder="Your name"
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30"
                  />
                </div>

                <!-- Email -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Email *</label>
                  <input
                    v-model="contactForm.email"
                    type="email"
                    required
                    placeholder="you@example.com"
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30"
                  />
                </div>

                <!-- Inquiry Type -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Inquiry Type *</label>
                  <select
                    v-model="contactForm.inquiryType"
                    required
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30 appearance-none"
                  >
                    <option value="" disabled class="text-slate/50">Select type</option>
                    <option value="Admissions">Admissions</option>
                    <option value="Partnerships">Partnerships</option>
                    <option value="Media">Media</option>
                    <option value="Careers">Careers</option>
                    <option value="General">General</option>
                  </select>
                </div>

                <!-- Subject -->
                <div>
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Subject *</label>
                  <input
                    v-model="contactForm.subject"
                    type="text"
                    required
                    placeholder="What is this regarding?"
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30"
                  />
                </div>

                <!-- Message -->
                <div class="md:col-span-2">
                  <label class="block text-xs font-semibold uppercase tracking-widest text-slate mb-2">Message *</label>
                  <textarea
                    v-model="contactForm.message"
                    rows="5"
                    required
                    placeholder="How can we help?"
                    class="w-full rounded-lg border border-off-white/10 bg-navy-light px-4 py-3.5 text-white placeholder-slate/50 outline-none transition-all duration-300 focus:border-gold focus:ring-1 focus:ring-gold/30 resize-none"
                  ></textarea>
                </div>
              </div>

              <div class="mt-8">
                <button
                  type="submit"
                  :disabled="contactSubmitting"
                  class="w-full sm:w-auto inline-flex items-center justify-center gap-2 rounded-lg bg-gold px-10 py-4 text-sm font-semibold uppercase tracking-widest text-navy transition-all duration-300 hover:bg-gold-light hover:shadow-lg hover:shadow-gold/20 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <svg v-if="contactSubmitting" class="animate-spin h-4 w-4" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                  </svg>
                  {{ contactSubmitting ? 'Sending...' : 'Send Message' }}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
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

.form-fade-enter-active,
.form-fade-leave-active {
  transition: all 0.35s cubic-bezier(0.22, 1, 0.36, 1);
}

.form-fade-enter-from {
  opacity: 0;
  transform: translateX(16px);
}

.form-fade-leave-to {
  opacity: 0;
  transform: translateX(-16px);
}

/* Style select dropdowns for dark backgrounds */
select option {
  background-color: var(--color-navy-light);
  color: white;
}
</style>
