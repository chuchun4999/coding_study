import Link from "next/link";
import './globals.css';


export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <h1>Title</h1>
        <script src="./dropdown.js"></script>
        <script src="https://kit.fontawesome.com/5a4cf82ee5.js" crossorigin="anonymous"></script>
        <link rel="preconnect" href="https://fonts.googleapis.com"/>
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
        <link href="https://fonts.googleapis.com/css2?family=Protest+Riot&display=swap" rel="stylesheet"></link>
        <ul className="navbar">
          <li><Link href="/">Home</Link></li>
          <li><Link href="/list">List</Link></li>
          <li><Link href="/about">About</Link></li>
        </ul>
        <div className="dropDown">
          <i className="fa-solid fa-bars"></i>
          <div className="subMenu">
            <a>Menu1</a>
            <a>Menu2</a>
            <a>Menu3</a>
          </div>
        </div>       
      </head>
      <body>
        {children}
      </body>
    </html>
  )
} 