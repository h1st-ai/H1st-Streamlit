import * as React from "react";
import { Col, Layout as AntLayout, Row, Image } from "antd";
import { Link } from "@reach/router";

const { Header, Content, Footer } = AntLayout;

interface LayoutProps {
  children?: JSX.Element;
}

const Layout = ({ children }: LayoutProps): JSX.Element => {
  return (
    <AntLayout style={{ minHeight: "100vh" }}>
      <Header style={{ backgroundColor: "#F7F8FC" }}>
        <Row justify="space-between" align="middle">
          <Col>
            <Link to={"/"}>
              <Image
                src="/img/logo.svg"
                style={{ height: 36, width: "auto", marginTop: 12 }}
                preview={false}
              />
            </Link>
          </Col>
        </Row>
      </Header>
      <Content style={{ padding: 24 }}>{children}</Content>
      <Footer>@H1st</Footer>
    </AntLayout>
  );
};

export { Layout };
