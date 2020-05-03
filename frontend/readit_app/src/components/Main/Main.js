import React, { Component, Fragment } from "react";
import logo from "../assets/taxi-2.svg";
import title from "../assets/Readit.svg";
import { Row, Col } from "react-bootstrap";
import "./Main.css";

class Main extends Component {
  render() {
    return (
      <div>
        <Row>
          <Col className="leftCol" lg={4}>
            <img src={logo} className="landing__logo" alt="leftside" />
          </Col>
          <Col className="rightCol" lg={8}>
            <Row className="justify-content-center">
              <Row className="logoContainer justify-content-center">
                <img src={title} className="logo" alt="readit" />
              </Row>
              <Row className="loginButtonContainer justify-content-center">
                <button className="loginButton">Log In</button>
              </Row>
              <Row className="signupButtonContainer justify-content-center">
                <button className="signupButton">Sign Up</button>
              </Row>
              <Row className="whyUsContainer justify-content-center">
                <button className="whyUsButton">Why us</button>
              </Row>
            </Row>
          </Col>
        </Row>
      </div>
    );
  }
}
export default Main;

// <div className="landing__logo-container">
// <div className="col">
//   <img src={logo} className="landing__logo"/>
// </div>
// <div className="row justify-content-center">
//   {/* <NavLink to="/login">
//     <Button type="primary">Get Started</Button>
//   </NavLink> */}
//   <img src={title} className="title-logo"/>

// </div>
// </div>
