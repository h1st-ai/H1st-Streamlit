import { Button, Card, Col, Input, notification, Row } from "antd";
import axios from "axios";
import React, { useRef, useState } from "react";
import CanvasDraw from "react-canvas-draw";
import { v4 as uuidv4 } from "uuid";

import Resizer from "react-image-file-resizer";

const resizeImage = (file: File, size = 100): Promise<any> =>
  new Promise((resolve) => {
    Resizer.imageFileResizer(
      file,
      size,
      size,
      "PNG",
      100,
      0,
      (uri) => {
        resolve(uri);
      },
      "base64"
    );
  });

function dataURLtoFile(dataurl: string, filename: string) {
  const arr = dataurl.split(",");
  const mime = arr?.[0]?.match(/:(.*?);/)?.[1];
  const bstr = atob(arr[1]);
  let n: number = bstr.length ?? 0;
  const u8arr = new Uint8Array(n);

  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }

  return new File([u8arr], filename, { type: mime });
}

const DrawCanvas = (props: any) => {
  const [predictedNumber, setPredictedNumber] = useState(null);
  const [resizedFile, setResizedFile] = useState<File | null>();
  const [showRightInput, setShowRightInput] = useState<boolean>(false);
  const [rightNumber, setRightNumber] = useState();
  const canvasRef = useRef();
  const handleOnChange = (canvas: any) => {
    if (!canvasRef.current) {
      canvasRef.current = canvas;
    }
  };

  const handleOnClassify = async () => {
    if (canvasRef.current) {
      const dataUrl = (canvasRef?.current as any)?.canvasContainer?.childNodes[1].toDataURL();
      const file = dataURLtoFile(dataUrl, "image.png");

      const resizedFileUrl = await resizeImage(file, 100);
      const resizedFile = dataURLtoFile(resizedFileUrl, `${uuidv4()}.png`);

      const formData = new FormData();
      formData.append("file", resizedFile);

      setResizedFile(resizedFile);

      const res = await axios.post(
        `${process.env.REACT_APP_BACKEND_URL}/predict_number`,
        formData
      );

      setPredictedNumber(res?.data?.prediction);
    }
  };

  const requestFeedback = async (formData: any) => {
    try {
      await axios.post(
        `${process.env.REACT_APP_BACKEND_URL}/feedback`,
        formData
      );

      notification.success({
        message: "Feedback sent sucessfully",
      });

      setPredictedNumber(null);
      setResizedFile(null);
      (canvasRef.current as any)?.clear?.();
      props?.getPredictions();
      setShowRightInput(false);
      setRightNumber(undefined);
    } catch {}
  };

  const sendFeedback = (feedback: boolean) => async () => {
    if (resizedFile && (predictedNumber || predictedNumber === 0)) {
      const formData = new FormData();
      formData.append("file", resizedFile);
      formData.append("prediction", predictedNumber as any);
      formData.append("feedback", feedback as any);
      requestFeedback(formData as any);
    }
  };

  const handleIncorrect = () => {
    setShowRightInput(true);
  };

  const submitIncorrect = () => {
    if (resizedFile && (predictedNumber || predictedNumber === 0)) {
      const formData = new FormData();
      formData.append("file", resizedFile);
      formData.append("prediction", predictedNumber as any);
      formData.append("feedback", "false");
      formData.append("correct_number", rightNumber as any);
      requestFeedback(formData as any);
    }
  };

  const onClearCanvas = () => {
    if (canvasRef.current) {
      // console.log(canvasRef?.current?.clear?.());
      (canvasRef.current as any)?.clear?.();
      setPredictedNumber(null);
    }
  };

  return (
    <Card style={{ height: "100%" }}>
      <Row style={{ fontSize: 18, marginBottom: 24 }}>
        Write your number here and click classify button
      </Row>
      <Row justify="center">
        <Col>
          <CanvasDraw
            canvasHeight={200}
            canvasWidth={200}
            hideGrid={true}
            lazyRadius={0}
            brushRadius={7}
            onChange={handleOnChange}
            style={{
              border: "1px solid black",
            }}
          />
        </Col>
      </Row>
      <Row justify="center" style={{ marginTop: 24 }}>
        <Col>
          <Button.Group>
            <Button type="primary" onClick={() => handleOnClassify()}>
              Classify
            </Button>
            <Button onClick={() => onClearCanvas()}>Clear</Button>
          </Button.Group>
        </Col>
      </Row>
      {(predictedNumber || predictedNumber === 0) && (
        <Row gutter={[16, 16]} style={{ marginTop: 24 }}>
          <Col span={24} style={{ fontSize: 24 }}>
            Prediction number:
            <span style={{ fontSize: 28 }}>{predictedNumber}</span>
          </Col>
          <Col span={24}>
            <Row justify="center" align="middle" style={{ width: "100%" }}>
              <Button.Group>
                <Button type="primary" onClick={sendFeedback(true)}>
                  Correct
                </Button>
                <Button type="default" onClick={handleIncorrect}>
                  Incorrect
                </Button>
              </Button.Group>
            </Row>
            {showRightInput && (
              <div>
                <Row justify="center" style={{ marginTop: 24, fontSize: 16 }}>
                  <Col span={24}>Please input the correct number:</Col>
                  <Col span={12}>
                    <Input
                      type="number"
                      onChange={(e) => setRightNumber(e.target.value as any)}
                    />
                  </Col>
                </Row>
                <Row justify="center" style={{ marginTop: 12 }}>
                  <Button onClick={() => submitIncorrect()}>Submit</Button>
                </Row>
              </div>
            )}
          </Col>
        </Row>
      )}
    </Card>
  );
};

export { DrawCanvas };
