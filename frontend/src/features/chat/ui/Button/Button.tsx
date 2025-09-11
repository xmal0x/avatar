import { ButtonHTMLAttributes } from "react"


const Button = (props: ButtonHTMLAttributes<HTMLButtonElement>) => {
  return (
    <button
      {...props}
      style={{
        padding: '10px 20px',
        borderRadius: 12,
        border: '1px solid #d0d7de',
        background: props.disabled ? '#d0d7de' : '#111',
        color: '#fff',
        cursor: 'pointer',
      }}
    />
  )
}

export default Button