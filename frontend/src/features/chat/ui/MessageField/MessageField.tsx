import { forwardRef, InputHTMLAttributes } from "react"

const MessageField = forwardRef<HTMLInputElement, InputHTMLAttributes<HTMLInputElement>>((props, ref) => {
  return (
      <input
        {...props}
        type="text"
        ref={ref}
        placeholder="Type your message here..."
        style={{
          width: '100%',
          padding: '10px 20px',
          borderRadius: 12,
          border: '1px solid #d0d7de',
          background: '#fff',
          color: '#111',
        }}
      />
  )
})

export default MessageField