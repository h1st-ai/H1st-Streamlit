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
          {
            title: "Correct number",
            dataIndex: "correct_number",
            align: "center",
          },
          {
            title: "Feedback",
            dataIndex: "feedback",
            render: (feedback) => (
              <Tag color={feedback ? "blue" : "orange"}>
                {feedback ? "Correct" : "Incorrect"}
              </Tag>
            ),
          },
        ]}
        dataSource={props?.predictions}
        rowKey="id"
      ></Table>
    </Card>
  );
};

const getSampleObj = () =>
  Array(10)
    .fill(0)
    .reduce((obj, _, i) => {
      obj[i] = {
        total: 0,
        correct: 0,
        rate: 0,
      };

      return obj;
    }, {});

const PredictionChart = (props: any) => {
  const data = useMemo(() => {
    const aggregated = props?.predictions?.reduce(
      (obj: any, predictionItem: any) => {
        const { prediction, feedback } = predictionItem;
        if (!obj[prediction]) {
          obj[prediction] = {
            total: 0,
            correct: 0,
            rate: 0,
          };
        }

        obj[prediction].total += 1;
        if (feedback) obj[prediction].correct += 1;

        obj[prediction].rate =
          (obj[prediction].correct / obj[prediction].total) * 100;

        return obj;
      },
      getSampleObj()
    );

    return Object.keys(aggregated).map((key) => ({
      ...aggregated[key],
      title: key,
    }));
  }, [props?.predictions]);

  console.log("analysis data", {
    data,
  });
  return (
    <Card title="Prediction analysis">
      <PredictionAnalysis data={data} />
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
      <Row gutter={[16, 16]}>
        {/* Drawing panel */}
        <Col span={8}>
          <DrawCanvas getPredictions={getPredictions} />
        </Col>
        {/* Prediction tables */}
        <Col span={16}>
          <PredictionTable predictions={predictions} />
        </Col>
        {/* Graph visualization */}
        <Col span={24}>
          <PredictionChart predictions={predictions} />
        </Col>
      </Row>
    </Layout>
  );
};

export default Dashboard;
