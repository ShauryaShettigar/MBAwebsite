<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { RouterLink, useRoute } from 'vue-router'

const isOpen = ref(false)
const scrolled = ref(false)
const route = useRoute()

const navLinks = [
  { name: 'Why Us', path: '/why-us' },
  { name: 'Program', path: '/program' },
  { name: 'Learning Model', path: '/learning-model' },
  { name: 'Industry', path: '/industry' },
  { name: 'Careers', path: '/careers' },
  { name: 'Insights', path: '/insights' },
  { name: 'Admissions', path: '/admissions' },
]

const handleScroll = () => {
  scrolled.value = window.scrollY > 20
}

onMounted(() => window.addEventListener('scroll', handleScroll))
onUnmounted(() => window.removeEventListener('scroll', handleScroll))

const closeMenu = () => { isOpen.value = false }
</script>

<template>
  <nav
    class="fixed top-0 left-0 right-0 z-50 transition-all duration-300"
    :class="scrolled ? 'bg-navy/95 backdrop-blur-md shadow-lg' : 'bg-transparent'"
  >
    <div class="max-w-7xl mx-auto px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        <!-- Logo -->
        <RouterLink to="/" class="flex items-center gap-3 group" @click="closeMenu">
          <div class="w-10 h-10 rounded-full border-2 border-gold flex items-center justify-center">
            <span class="text-gold font-display font-bold text-lg">A</span>
          </div>
          <div class="flex flex-col">
            <span class="text-white font-display text-lg font-semibold tracking-wide leading-tight">AUREUM</span>
            <span class="text-gold/80 text-[10px] tracking-[0.25em] uppercase">School of Finance</span>
          </div>
        </RouterLink>

        <!-- Desktop Nav -->
        <div class="hidden lg:flex items-center gap-1">
          <RouterLink
            v-for="link in navLinks"
            :key="link.path"
            :to="link.path"
            class="px-3 py-2 text-sm text-white/70 hover:text-white transition-colors relative group"
            active-class="!text-gold"
          >
            {{ link.name }}
            <span class="absolute bottom-0 left-3 right-3 h-px bg-gold scale-x-0 group-hover:scale-x-100 transition-transform origin-left" />
          </RouterLink>
        </div>

        <!-- Desktop CTAs -->
        <div class="hidden lg:flex items-center gap-4">
          <RouterLink
            to="/contact"
            class="text-sm text-white/70 hover:text-white transition-colors"
          >
            Contact
          </RouterLink>
          <RouterLink
            to="/admissions"
            class="bg-gold hover:bg-gold-dark text-navy font-semibold text-sm px-5 py-2.5 rounded transition-colors"
          >
            Apply Now
          </RouterLink>
        </div>

        <!-- Mobile toggle -->
        <button
          class="lg:hidden text-white p-2"
          @click="isOpen = !isOpen"
          aria-label="Toggle menu"
        >
          <svg v-if="!isOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    <Transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-2"
    >
      <div v-if="isOpen" class="lg:hidden bg-navy/98 backdrop-blur-md border-t border-white/10">
        <div class="px-6 py-4 space-y-1">
          <RouterLink
            v-for="link in navLinks"
            :key="link.path"
            :to="link.path"
            class="block px-4 py-3 text-white/70 hover:text-white hover:bg-white/5 rounded-lg transition-colors"
            active-class="!text-gold !bg-gold/5"
            @click="closeMenu"
          >
            {{ link.name }}
          </RouterLink>
          <div class="pt-4 border-t border-white/10 flex flex-col gap-3">
            <RouterLink
              to="/contact"
              class="block px-4 py-3 text-white/70 hover:text-white transition-colors"
              @click="closeMenu"
            >
              Contact
            </RouterLink>
            <RouterLink
              to="/admissions"
              class="block text-center bg-gold hover:bg-gold-dark text-navy font-semibold py-3 rounded transition-colors"
              @click="closeMenu"
            >
              Apply Now
            </RouterLink>
          </div>
        </div>
      </div>
    </Transition>
  </nav>
</template>
