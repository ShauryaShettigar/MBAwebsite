<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { ref, computed, onMounted, onUnmounted } from 'vue'

const activeFilter = ref<string>('All')

const categories = ['All', 'Reports', 'Articles', 'Podcasts', 'Events'] as const

const featuredInsight = {
  title: 'The ₹15 Lakh Question: Why India\'s Finance Education Needs a Reset',
  category: 'Report',
  date: 'March 2026',
  excerpt:
    'A deep-dive analysis into the structural misalignment between what India\'s finance industry demands and what traditional MBA programs deliver. Drawing on placement data, employer surveys, and global benchmarks, this report makes the case for a fundamentally different approach to finance education.',
}

const insights = [
  {
    title: 'CXO Podcast: The Future of Investment Banking in India',
    category: 'Podcast',
    date: 'February 2026',
    excerpt:
      'Senior investment bankers discuss how deal-making in India is evolving and what it means for the next generation of finance professionals.',
  },
  {
    title: 'Why Practitioner-Led Teaching Produces Better Outcomes',
    category: 'Article',
    date: 'January 2026',
    excerpt:
      'Evidence from global finance programs suggests that practitioner faculty drive measurably higher career readiness among graduates.',
  },
  {
    title: 'India\'s BFSI Talent Gap: A Data-Driven Analysis',
    category: 'Report',
    date: 'December 2025',
    excerpt:
      'New research quantifies the skills deficit across banking, financial services, and insurance, and identifies the competencies employers struggle to find.',
  },
  {
    title: 'From Classroom to Trading Floor: Bridging the Readiness Gap',
    category: 'Article',
    date: 'November 2025',
    excerpt:
      'How immersive, project-based learning models can compress the ramp-up time for new hires entering capital markets roles.',
  },
  {
    title: 'Event Recap: Finance Leaders Summit 2025',
    category: 'Event',
    date: 'October 2025',
    excerpt:
      'Key takeaways from India\'s premier gathering of finance education stakeholders, featuring panels on curriculum reform and industry collaboration.',
  },
  {
    title: 'Building an Institution-Grade Education Brand',
    category: 'Article',
    date: 'September 2025',
    excerpt:
      'Lessons from the world\'s top finance schools on how institutional credibility is built through rigour, selectivity, and industry alignment.',
  },
]

const filteredInsights = computed(() => {
  if (activeFilter.value === 'All') return insights
  const plural = activeFilter.value
  const singular = plural.endsWith('s') ? plural.slice(0, -1) : plural
  return insights.filter((i) => i.category === singular)
})

function categoryColor(category: string): string {
  switch (category) {
    case 'Report':
      return 'bg-gold/15 text-gold'
    case 'Article':
      return 'bg-emerald-500/15 text-emerald-400'
    case 'Podcast':
      return 'bg-violet-500/15 text-violet-400'
    case 'Event':
      return 'bg-sky-500/15 text-sky-400'
    default:
      return 'bg-slate/15 text-slate'
  }
}

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
            <span class="text-gold text-sm tracking-widest uppercase font-medium">Thought Leadership</span>
          </div>

          <h1 class="font-display text-4xl md:text-5xl lg:text-6xl text-white font-bold leading-tight mb-8">
            Insights <span class="text-gold">&amp; Ideas</span>
          </h1>

          <p class="text-lg md:text-xl text-slate leading-relaxed max-w-2xl">
            Perspectives from the intersection of finance, education, and industry.
          </p>
        </div>
      </div>
    </section>

    <!-- ============================================ -->
    <!-- FEATURED INSIGHT -->
    <!-- ============================================ -->
    <section class="py-20 md:py-28 bg-off-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="fade-up">
          <a
            href="#"
            class="group block rounded-2xl bg-navy overflow-hidden transition-all duration-500 hover:shadow-2xl hover:shadow-gold/10"
          >
            <div class="grid md:grid-cols-2">
              <!-- Visual panel -->
              <div class="relative h-64 md:h-auto bg-gradient-to-br from-navy-light to-navy flex items-center justify-center overflow-hidden">
                <div class="absolute inset-0 bg-[radial-gradient(circle_at_30%_50%,_var(--color-gold)_0%,_transparent_50%)] opacity-10" />
                <div class="relative text-center px-8">
                  <span class="inline-block px-4 py-1.5 rounded-full text-xs font-semibold uppercase tracking-widest bg-gold/15 text-gold mb-4">
                    Featured
                  </span>
                  <div class="w-20 h-px bg-gold/30 mx-auto" />
                </div>
              </div>

              <!-- Content panel -->
              <div class="p-8 md:p-12 lg:p-16 flex flex-col justify-center">
                <div class="flex items-center gap-3 mb-6">
                  <span class="inline-block px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider bg-gold/15 text-gold">
                    {{ featuredInsight.category }}
                  </span>
                  <span class="text-sm text-slate">{{ featuredInsight.date }}</span>
                </div>

                <h2 class="font-display text-2xl md:text-3xl lg:text-4xl text-white font-bold leading-snug mb-6 group-hover:text-gold transition-colors duration-300">
                  {{ featuredInsight.title }}
                </h2>

                <p class="text-slate leading-relaxed mb-8">
                  {{ featuredInsight.excerpt }}
                </p>

                <div class="flex items-center gap-2 text-gold font-semibold text-sm uppercase tracking-widest">
                  <span>Read More</span>
                  <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
                  </svg>
                </div>
              </div>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- ============================================ -->
    <!-- CONTENT GRID WITH FILTERS -->
    <!-- ============================================ -->
    <section class="py-20 md:py-28 bg-cream">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <!-- Filter Tabs -->
        <div class="fade-up mb-16 flex flex-wrap gap-3">
          <button
            v-for="cat in categories"
            :key="cat"
            @click="activeFilter = cat"
            class="px-5 py-2.5 rounded-full text-sm font-semibold tracking-wide transition-all duration-300"
            :class="
              activeFilter === cat
                ? 'bg-navy text-gold shadow-lg shadow-navy/20'
                : 'bg-white text-charcoal/60 border border-charcoal/10 hover:border-gold/30 hover:text-navy'
            "
          >
            {{ cat }}
          </button>
        </div>

        <!-- Cards Grid -->
        <div class="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
          <TransitionGroup name="card">
            <a
              v-for="insight in filteredInsights"
              :key="insight.title"
              href="#"
              class="fade-up group flex flex-col rounded-2xl bg-white border border-charcoal/5 overflow-hidden transition-all duration-300 hover:border-gold/20 hover:shadow-xl hover:shadow-gold/5"
            >
              <!-- Card top accent -->
              <div class="h-1 w-full bg-gradient-to-r from-gold/40 via-gold to-gold/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

              <div class="flex flex-col flex-1 p-7 sm:p-8">
                <div class="flex items-center gap-3 mb-5">
                  <span
                    class="inline-block px-3 py-1 rounded-full text-[11px] font-semibold uppercase tracking-wider"
                    :class="categoryColor(insight.category)"
                  >
                    {{ insight.category }}
                  </span>
                  <span class="text-xs text-charcoal/40">{{ insight.date }}</span>
                </div>

                <h3 class="font-display text-lg md:text-xl text-navy font-bold leading-snug mb-4 group-hover:text-gold-dark transition-colors duration-300">
                  {{ insight.title }}
                </h3>

                <p class="text-sm text-charcoal/60 leading-relaxed mb-6 flex-1">
                  {{ insight.excerpt }}
                </p>

                <div class="flex items-center gap-2 text-gold-dark font-semibold text-xs uppercase tracking-widest">
                  <span>Read More</span>
                  <svg class="w-3.5 h-3.5 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
                  </svg>
                </div>
              </div>
            </a>
          </TransitionGroup>
        </div>

        <!-- Empty state -->
        <div v-if="filteredInsights.length === 0" class="text-center py-20">
          <p class="text-charcoal/40 text-lg">No insights found in this category yet.</p>
        </div>
      </div>
    </section>

    <!-- ============================================ -->
    <!-- SUBSCRIBE CTA -->
    <!-- ============================================ -->
    <section class="bg-navy py-20 sm:py-24">
      <div class="max-w-4xl mx-auto px-6 lg:px-8 text-center">
        <div class="fade-up">
          <p class="text-xs font-semibold uppercase tracking-[0.25em] text-gold mb-4">Stay Informed</p>
          <h2 class="font-display text-3xl md:text-4xl text-white font-bold mb-6">
            Never Miss an Insight
          </h2>
          <p class="text-slate text-lg leading-relaxed max-w-2xl mx-auto mb-10">
            Subscribe to our newsletter for the latest research, analysis, and perspectives
            from the Aureum community. Delivered monthly to your inbox.
          </p>
          <RouterLink
            to="/contact"
            class="inline-flex items-center gap-2 rounded-sm border border-gold px-8 py-4 text-sm font-semibold uppercase tracking-widest text-gold transition-all duration-300 hover:bg-gold hover:text-navy"
          >
            Subscribe in Footer
            <svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </RouterLink>
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

.card-enter-active,
.card-leave-active {
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}

.card-enter-from {
  opacity: 0;
  transform: translateY(20px) scale(0.97);
}

.card-leave-to {
  opacity: 0;
  transform: translateY(-10px) scale(0.97);
}

.card-move {
  transition: transform 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}
</style>
