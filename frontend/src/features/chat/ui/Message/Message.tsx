import { Message as MessageInterface } from "../../api/chatApi"

interface Props {
  message: MessageInterface
}

const Message = ({ message }: Props) => {
  return (
    <div
      style={{ padding: 10, borderRadius: 12, backgroundColor: message.role === 'user' ? 'lightgray' : 'lightblue', maxWidth: '90%', alignSelf: message.role === 'user' ? 'flex-end' : 'flex-start' }}
    >
      {message.message}
    </div>
  )
}

export default Message