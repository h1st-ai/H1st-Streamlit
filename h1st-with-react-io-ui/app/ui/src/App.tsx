import React, { lazy, Suspense } from "react";
import { Router } from "@reach/router";
import "antd/dist/antd.less";
import "./App.css";
import { Spin } from "antd";

const Dashboard = lazy(() => import("./views/Dashboard"));
const WaitingComponent = ({
  Component,
  path,
  ...props
}: {
  Component: any;
  path: string;
}) => (
  <Suspense fallback={<Spin />}>
    <Component path={path} {...props} />
  </Suspense>
);

function App() {
  return (
    <Suspense fallback={<Spin />}>
      <Router>
        <WaitingComponent Component={Dashboard} path="/" />
      </Router>
    </Suspense>
  );
}

export default App;
