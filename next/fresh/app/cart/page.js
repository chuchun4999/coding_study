import age from "./data.js"
export default function Cart() {
    return (
      <div>
        <h4 className="title">Cart</h4>
        <div className="cart-item">
          <p>상품명 {age}</p>
          <p>$40</p>
          <p>1개</p>
        </div>
        <CartItem/>
        <CartItem/>
      </div>
    )
  }

  function CartItem(props){
    return(
        <div className="cart-item">
          <p>상품명</p>
          <p>$40</p>
          <p>1개</p>
        </div>
    )
  }