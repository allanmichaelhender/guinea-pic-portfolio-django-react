import React from "react";
import { useForm } from "react-hook-form";
import axios from "axios";
import api from "../api";

const PortfoliosForm = ({ onSourceChange }) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    defaultValues: {
      investment_amount: 0,
      FTSE_weight: 0,
      SNP500_weight: 0,
      NIKKEI225_weight: 0,
    },
  });

  const today = new Date().toISOString().split("T")[0];

  const onSubmit = async (data) => {
    try {
      const response = await api.post("/api/portfolios/", data);
      alert("Portfolio Created!");
      onSourceChange();
    } catch (error) {
      console.error("Submission failed:", error.response?.data);
    }
  };

  const onError = (errors) => console.log("Form Validation Errors:", errors);

  return (
    <form onSubmit={handleSubmit(onSubmit, onError)}>
      <div className="investment-frequency-input-field">
        <label>Investment Frequency:</label>
        <input
          type="radio"
          value="daily"
          {...register("investment_frequency")}
        />{" "}
        Daily
        <input
          type="radio"
          value="monthly"
          {...register("investment_frequency")}
        />{" "}
        Monthly
      </div>

      <input
        type="number"
        className="amount-input"
        step="0.01"
        {...register("investment_amount", { valueAsNumber: true })}
      />

      <input
        type="date"
        className="date-input-field"
        {...register("start_date", {
          required: "A date is required",
          min: {
            value: "2015-01-01",
            message: "Date cannot be before January 1st, 2015",
          },
          max: {
            value: today,
            message: "Date cannot be in the future",
          },
        })}
      />
      {errors.start_date && <span>{errors.start_date.message}</span>}
      <input
        type="date"
        className="date-input-field"
        {...register("end_date", {
          required: "A date is required",
          min: {
            value: "2015-01-01",
            message: "Date cannot be before January 1st, 2015",
          },
          max: {
            value: today,
            message: "Date cannot be in the future",
          },
        })}
      />
      {errors.end_date && <span>{errors.end_date.message}</span>}

      <input
        type="number"
        step="0.01"
        className="weight-input"
        {...register("FTSE_weight", { valueAsNumber: true })}
      />

      <input
        type="number"
        step="0.01"
        className="weight-input"
        {...register("SNP500_weight", { valueAsNumber: true })}
      />

      <input
        type="number"
        step="0.01"
        className="weight-input"
        {...register("NIKKEI225_weight", { valueAsNumber: true })}
      />



      <button type="submit">Submit Portfolio</button>
    </form>
  );
};

export default PortfoliosForm;
