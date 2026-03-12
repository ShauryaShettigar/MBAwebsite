<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { subscribeNewsletter } from '@/lib/api'

const email = ref('')
const status = ref<'idle' | 'loading' | 'success' | 'error'>('idle')

const handleSubscribe = async () => {
  if (!email.value) return
  status.value = 'loading'
  try {
    await subscribeNewsletter(email.value)
    status.value = 'success'
    email.value = ''
    setTimeout(() => { status.value = 'idle' }, 3000)
  } catch {
    status.value = 'error'
    setTimeout(() => { status.value = 'idle' }, 3000)
  }
}

const footerLinks = {
  Institution: [
    { name: 'Why Aureum', path: '/why-us' },
    { name: 'Program', path: '/program' },
    { name: 'Learning Model', path: '/learning-model' },
    { name: 'Industry Network', path: '/industry' },
  ],
  Admissions: [
    { name: 'Founding Cohort', path: '/admissions' },
    { name: 'Career Outcomes', path: '/careers' },
    { name: 'FAQs', path: '/admissions#faqs' },
    { name: 'Apply Now', path: '/admissions' },
  ],
  Connect: [
    { name: 'Contact Us', path: '/contact' },
    { name: 'Insights', path: '/insights' },
    { name: 'For Industry Leaders', path: '/contact#industry' },
    { name: 'Newsletter', path: '#newsletter' },
  ],
}
</script>

<template>
  <footer class="bg-navy text-white">
    <!-- Newsletter Section -->
    <div id="newsletter" class="border-b border-white/10">
      <div class="max-w-7xl mx-auto px-6 lg:px-8 py-16">
        <div class="max-w-2xl">
          <h3 class="font-display text-2xl lg:text-3xl font-semibold mb-3">
            Stay informed
          </h3>
          <p class="text-white/60 mb-6">
            Receive updates on admissions, industry events, and insights from finance leaders.
          </p>
          <form @submit.prevent="handleSubscribe" class="flex gap-3 max-w-md">
            <input
              v-model="email"
              type="email"
              required
              placeholder="Your email address"
              class="flex-1 bg-white/5 border border-white/10 rounded px-4 py-3 text-sm text-white placeholder-white/40 focus:outline-none focus:border-gold/50 transition-colors"
            />
            <button
              type="submit"
              :disabled="status === 'loading'"
              class="bg-gold hover:bg-gold-dark text-navy font-semibold text-sm px-6 py-3 rounded transition-colors whitespace-nowrap disabled:opacity-50"
            >
              {{ status === 'loading' ? 'Subscribing...' : 'Subscribe' }}
            </button>
          </form>
          <p v-if="status === 'success'" class="text-emerald-400 text-sm mt-3">
            Successfully subscribed!
          </p>
          <p v-if="status === 'error'" class="text-red-400 text-sm mt-3">
            Something went wrong. Please try again.
          </p>
        </div>
      </div>
    </div>

    <!-- Links Grid -->
    <div class="max-w-7xl mx-auto px-6 lg:px-8 py-16">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-8 lg:gap-12">
        <!-- Brand Column -->
        <div class="col-span-2 md:col-span-1">
          <div class="flex items-center gap-3 mb-4">
            <div class="w-9 h-9 rounded-full border-2 border-gold flex items-center justify-center">
              <span class="text-gold font-display font-bold">A</span>
            </div>
            <div class="flex flex-col">
              <span class="text-white font-display font-semibold tracking-wide text-sm">AUREUM</span>
              <span class="text-gold/60 text-[9px] tracking-[0.2em] uppercase">School of Finance</span>
            </div>
          </div>
          <p class="text-white/40 text-sm leading-relaxed">
            A new standard for finance education. Industry-built. Practitioner-led. Day-1 ready.
          </p>
          <p class="text-white/30 text-sm mt-4">Mumbai, India</p>
        </div>

        <!-- Link Columns -->
        <div v-for="(links, category) in footerLinks" :key="category">
          <h4 class="text-white/50 uppercase text-xs tracking-wider font-semibold mb-4">
            {{ category }}
          </h4>
          <ul class="space-y-3">
            <li v-for="link in links" :key="link.path">
              <RouterLink
                :to="link.path"
                class="text-sm text-white/60 hover:text-white transition-colors"
              >
                {{ link.name }}
              </RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div class="border-t border-white/10">
      <div class="max-w-7xl mx-auto px-6 lg:px-8 py-6 flex flex-col md:flex-row justify-between items-center gap-4">
        <p class="text-white/30 text-sm">
          &copy; {{ new Date().getFullYear() }} Aureum School of Finance. All rights reserved.
        </p>
        <div class="flex items-center gap-6">
          <a href="#" class="text-white/30 hover:text-white/60 text-sm transition-colors">Privacy Policy</a>
          <a href="#" class="text-white/30 hover:text-white/60 text-sm transition-colors">Terms</a>
        </div>
      </div>
    </div>
  </footer>
</template>
