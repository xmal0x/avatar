
import { useChatStore } from "../../store/chatStore";
import MessageInput from "../MessageInput/MessageInput";
import MessageList from "../MessageList/MessageList";

export default function ChatPage() {
  const { messages, loading, error, send } = useChatStore();

  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', padding: 24, display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
      <MessageList messages={messages} />
      <MessageInput onSend={send} loading={loading} />
      {error && <p>{error}</p>}
    </div>
  )
}