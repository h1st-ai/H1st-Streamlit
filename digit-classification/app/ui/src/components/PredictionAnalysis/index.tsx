import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  LabelList,
} from "recharts";

const PredictionAnalysis = (props: any) => {
  return (
    <ResponsiveContainer width="95%" height={400}>
      <BarChart
        data={props?.data}
        margin={{
          top: 40,
          right: 30,
          left: 20,
          bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="title" />
        <YAxis min={0} max={100} />
        <Tooltip />
        <Legend />
        <Bar dataKey="rate" fill="#2241B0">
          {/* <LabelList dataKey="name" angle="45" /> */}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
};

export { PredictionAnalysis };
