import { InboxOutlined } from "@ant-design/icons";
import { Modal, Upload, message } from "antd";
import * as React from "react";

interface UploadModalProps {
  visible: boolean;
  setVisible: Function;
  onSuccess?: Function;
}

const { Dragger } = Upload;

const UploadModal = ({ visible, setVisible, onSuccess }: UploadModalProps) => {
  return (
    <Modal
      title="Upload"
      visible={visible}
      onCancel={() => setVisible(false)}
      bodyStyle={{ padding: 24 }}
      destroyOnClose={true}
    >
      <Dragger
        name="file"
        multiple={false}
        action={`${process.env.REACT_APP_BACKEND_URL}/upload`}
        accept=".csv,.zip"
        onChange={(info: any) => {
          const { status } = info.file;
          if (status !== "uploading") {
            console.log(info.file, info.fileList);
          }
          if (status === "done") {
            message.success(`${info.file.name} file uploaded successfully.`);
            onSuccess && onSuccess();
            setVisible(false);
          } else if (status === "error") {
            message.error(`${info.file.name} file upload failed.`);
          }
        }}
      >
        <p className="ant-upload-drag-icon">
          <InboxOutlined />
        </p>
        <p className="ant-upload-text">
          Click or drag file to this area to upload
        </p>
        <p className="ant-upload-hint">Supported file extensions: csv, zip</p>
      </Dragger>
    </Modal>
  );
};

export { UploadModal };
