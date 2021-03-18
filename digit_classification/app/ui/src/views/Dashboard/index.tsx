import { Card, Col, Row, Table, Tag } from "antd";
import axios from "axios";

import { useEffect, useMemo, useState } from "react";
import { DrawCanvas } from "../../components/DrawCanvas";
import { PredictionAnalysis } from "../../components/PredictionAnalysis";
import { Layout } from "../Layout";

const PredictionTable = (props: any) => {
  return (
    <Card title="Prediction table" style={{ height: "100%" }}>
      <Table
        columns={[
          {
            title: "ID",
            dataIndex: "id",
          },
          {
            title: "Image",
            dataIndex: "filename",
            render: (filename) => (
              <img
                src={`${process.env.REACT_APP_BACKEND_URL}/img_files/${filename}`}
                width={30}
                alt={filename}
              />
            ),
          },
          {
            title: "Prediction",
            dataIndex: "prediction",
            align: "center",
          },
        ]}
        dataSource={props?.predictions}
        rowKey="id"
      ></Table>
    </Card>
  );
};

const Dashboard = () => {
  const [predictions, setPredictions] = useState([]);

  const getPredictions = async () => {
    const res = await axios.get(
      `${process.env.REACT_APP_BACKEND_URL}/predictions`
    );
    console.log(res);
    setPredictions(res?.data ?? 0);
  };

  useEffect(() => {
    getPredictions();
  }, []);
  return (
    <Layout>
      <Row gutter={[16, 16]} justify="center">
        {/* Drawing panel */}
        <Col span={8}>
          <DrawCanvas getPredictions={getPredictions} />
        </Col>
        {/* Prediction tables */}
        <Col span={8}>
          <PredictionTable predictions={predictions} />
        </Col>
      </Row>
    </Layout>
  );
};

export default Dashboard;
