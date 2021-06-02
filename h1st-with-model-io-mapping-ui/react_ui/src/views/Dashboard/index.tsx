import axios from "axios";
import { useState } from "react";
import { Layout } from "../Layout";
import CONFIG from "config";

import styles from "./style.module.css";

const backendUrl =
  process.env.REACT_APP_AI_WORKFLOW_URL ?? "http://localhost:8000";

const Dashboard = () => {
  const appData = { title: "H1st React App" };
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");

  const handleOnSendData = async () => {
    try {
      const res = await axios.post(
        `${backendUrl}`,
        { payload: input },
        {
          auth: {
            username: process.env.REACT_APP_AI_USERNAME ?? "",
            password: process.env.REACT_APP_AI_PASSWORD ?? "",
          },
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      setOutput(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Layout {...CONFIG}>
      <div className={styles.gridWrapper}>
        <div className={styles.input}>
          <h3>English</h3>
          <textarea
            className={styles.textInput}
            rows={4}
            defaultValue=""
            onChange={(e) => setInput(e.target.value)}
          ></textarea>

          <button disabled={!input} onClick={handleOnSendData}>
            Translate
          </button>
        </div>
        <div className={styles.output}>
          <h3>Spanish</h3>
          <textarea
            className={styles.textInput}
            rows={4}
            value={output}
            disabled={true}
          ></textarea>
        </div>
      </div>
    </Layout>
  );
};

export default Dashboard;
