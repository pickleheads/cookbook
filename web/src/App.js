import React from 'react';
import logo from './chef.png';
import styled, { keyframes } from 'styled-components';

const AppContainter = styled.div`
  text-align: center;
`
const AppHeader = styled.header`
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
`
const AppLogoSpin = keyframes`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`
const AppLogo = styled.img`
  height: 40vmin;
  pointer-events: none;
  @media (prefers-reduced-motion: no-preference) {
    animation: ${AppLogoSpin} infinite 20s linear;
  }
`
const AppLink = styled.a`
  color: #61dafb;
`
function App() {
  return (
    <AppContainter>
      <AppHeader>
        <AppLogo src={logo} alt="logo"/>
        <p>Cooooooooooook</p>
        <AppLink
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
        And Boooooooook
        </AppLink>
      </AppHeader>
    </AppContainter>
  );
}

export default App;
