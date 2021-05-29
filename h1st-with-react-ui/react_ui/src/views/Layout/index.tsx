import * as React from "react";
import { Link } from "@reach/router";
import styles from "./styles.module.css";
import Logo from "./logo.svg";
interface LayoutProps {
  children?: JSX.Element;
  title?: string;
}

const Layout = ({ children, title }: LayoutProps): JSX.Element => {
  return (
    <div className={styles.layoutWrapper}>
      <div className={styles.header}>
        <div className={styles.content}>
          <Link to={"/"} className={styles.logoWrapper}>
            <img src={Logo} alt="Logo" /> {title}
          </Link>
        </div>
      </div>
      <div className={styles.contentWrapper}>
        <div className={styles.content}>{children}</div>
      </div>
      <div className={styles.footer}>
        <div className={styles.content}>
          Powered by{" "}
          <a href="https://github.com/h1st-ai" target="_blank" rel="noreferrer">
            H1st
          </a>
        </div>
      </div>
    </div>
  );
};

export { Layout };
