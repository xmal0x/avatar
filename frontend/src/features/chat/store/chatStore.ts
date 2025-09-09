import { create } from "zustand"
import { chatApi, Message } from "../api/chatApi"

type State = {
  messages: Message[]
  loading: boolean
  error: string | null
}

type Actions = {
  send: (text: string) => void
}

export const useChatStore = create<State & Actions>((set, get) => ({
  messages: [],
  loading: false,
  error: null,

  send: async (text: string) => {
    const trimmed = text.trim()
    if (!trimmed) return

    const id = Math.max(0, ...get().messages.map(m => m.id)) + 1
    const userMessage: Message = { id, message: trimmed, role: 'user' }
    set({ messages: [...get().messages, userMessage] })

    set({ loading: true, error: null })
    try {
      const response = await chatApi.send({ content: trimmed})
      set({ messages: [...get().messages, {id: id + 1, message: response.result, role: 'agent'}] })
    } catch (error) {
      set({ error: error as string }) 
    } finally {
      set({ loading: false })
    }
  }
}))