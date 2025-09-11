import { useRef, useState } from "react";
import Button from "../Button/Button";
import MessageField from "../MessageField/MessageField";

interface Props {
  onSend: (message: string) => void;
  loading: boolean;
}

const MessageInput = ({ onSend, loading }: Props) => {
  const [value, setValue] = useState('');
  const ref = useRef<HTMLInputElement>(null);

  const handleSend = () => {
    const trimmed = value.trim();
    if (!trimmed) return;
    onSend(trimmed);
    setValue('');
    ref.current?.focus();
  }
  
  return (
    <div style={{ display: 'flex', gap: 20, width: '100%', justifyContent: 'center' }}>
      <MessageField value={value} onChange={(e) => setValue(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && handleSend()} ref={ref} />
      <Button onClick={handleSend} disabled={loading}>Answer</Button>
    </div>
  )
}

export default MessageInput