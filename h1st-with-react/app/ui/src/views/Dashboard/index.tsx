import { Button, Card, Col, Input, Row } from "antd";
import axios from "axios";
import { useState } from "react";
import { Layout } from "../Layout";

const backendUrl = process.env.REACT_APP_BACKEND_URL ?? "http://localhost:8000";

const Dashboard = () => {
  const [content, setContent] = useState("");
  const [result, setResult] = useState();

  const handleOnSendData = async () => {
    try {
      const res = await axios.post(`${backendUrl}/predict`, content);
      setResult(res.data);
    } catch (error) {}
  };

  return (
    <Layout>
      <Row
        justify="center"
        align="middle"
        style={{ width: "100%", height: "100%" }}
      >
        <Col xs={22} md={16} lg={10}>
          <Card title="Prediction App">
            <Row gutter={[24, 24]}>
              <Col span={24}>
                <Input.TextArea onChange={(e) => setContent(e.target.value)} />
              </Col>
              <Col span={24}>
                <Row justify="center">
                  <Button onClick={handleOnSendData}>Send Data</Button>
                </Row>
              </Col>
              <Col span={24}>Result:</Col>
              <Col span={24}>{result}</Col>
            </Row>
          </Card>
        </Col>
      </Row>
    </Layout>
  );
};

export default Dashboard;
