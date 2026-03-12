import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

export const submitStudentLead = (data: Record<string, string>) =>
  api.post('/leads/student/', data)

export const submitIndustryLead = (data: Record<string, string>) =>
  api.post('/leads/industry/', data)

export const subscribeNewsletter = (email: string) =>
  api.post('/newsletter/', { email })

export const submitContactInquiry = (data: Record<string, string>) =>
  api.post('/contact/', data)

export default api
