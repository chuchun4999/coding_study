'use client'
import Script from 'next/script'
import { useEffect, useState } from 'react';
import data from './data';
export default function Home() {
  const [slideIndex, setSlideIndex] = useState(0);
  useEffect(() => {
    var slideIndex = 0;
    showSlides();
    function showSlides() {
      var i;
      var slides = document.getElementsByClassName("slide");
      for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
      }
      slideIndex++;
      if (slideIndex > slides.length) {
          slideIndex = 1;
      }
      slides[slideIndex - 1].style.display = "block";
      setTimeout(showSlides, 2000);  // 2초마다 이미지가 변경
    }
  }, []);
    
  return (
    <div>
      <div className="slide fade">
        <img src="https://img.freepik.com/free-photo/portrait-young-japanese-woman-with-jacket_23-2148870730.jpg?size=626&ext=jpg&ga=GA1.2.1990060104.1707462307&semt=ais"></img>
      </div>
      <div className="slide fade">
        <img style={{top:"-180px"}} src="https://img.freepik.com/free-photo/male-and-female-walking-in-different-directions_158595-5459.jpg?size=626&ext=jpg&ga=GA1.2.1990060104.1707462307&semt=ais"></img>
      </div>
      <div className="main">
        <h3>products</h3><br></br>
        <div className="product_cont">
          {
            data.map((data,i)=>{
              return (
                <Card data={data}></Card>
              )
            })
          }
        </div>      
      </div>
    </div>
  );
}

function Card({data}){
  return (
      <figure className="product" onclick="location.href='./list'">
      <img src={data[0]}></img>
      <figcaption>
        {data[1]}<br/>
        {data[2]}
      </figcaption>
    </figure>
    
  );
}