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

      const res = await axios.post(
        `${process.env.REACT_APP_BACKEND_URL}/predict_digit`,
        formData
      );

      setPredictedNumber(res?.data?.prediction);
      props?.getPredictions();
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
        </Row>
      )}
    </Card>
  );
};

export { DrawCanvas };
