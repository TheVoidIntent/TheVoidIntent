import os
import yaml
import logging
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# If you plan to use a deployment API (e.g., Cloudflare), you can import 'requests':
# import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class IntentAgent:
    def __init__(self, manifest_path: str = "intent_manifest.yaml"):
        """
        Initialize the IntentAgent with the path to the intent manifest.
        The manifest should contain the agent's core intent, directives, and values.
        """
        if not os.path.exists(manifest_path):
            raise FileNotFoundError(f"Manifest file not found: {manifest_path}")

        with open(manifest_path, "r") as mf:
            self.manifest = yaml.safe_load(mf)

        # Validate required keys in manifest
        required_keys = ["agent_name", "creator", "core_intent", "directives"]
        for key in required_keys:
            if key not in self.manifest:
                raise ValueError(f"Missing required key in manifest: '{key}'")

        self.agent_name = self.manifest["agent_name"]
        self.creator = self.manifest["creator"]
        self.core_intent = self.manifest["core_intent"]
        self.directives = self.manifest["directives"]

        logging.info(f"[{self.agent_name}] Initialized with core intent: {self.core_intent}")

    def act(self, task: str):
        """
        The central method where the agent interprets a requested task.
        Dispatches the task to the appropriate subroutine.
        """
        logging.info(f"[{self.agent_name}] Acting on task: '{task}'")

        # Simple dictionary-based dispatch for clarity/scalability
        dispatch_map = {
            "create_chart": self.create_chart,
            "update_site": self.update_site,
            "summarize_recent_data": self.summarize_recent_data,
        }

        # Find matching command or fallback
        if task in dispatch_map:
            dispatch_map[task]()
        else:
            logging.warning(
                f"[{self.agent_name}] No direct handler for task: '{task}'. "
                "Consider adding a new method or refining your instructions."
            )

    def create_chart(self, data_path: str = "data/simulation_output.csv"):
        """
        Loads CSV data (time, entropy, complexity, etc.) and generates
        a PNG chart (e.g., entropy over time).
        """
        try:
            if not os.path.exists(data_path):
                logging.error(f"Data file not found at: {data_path}")
                return

            df = pd.read_csv(data_path)

            # Expecting at least 'timestamp' and 'entropy' columns, but adjust to your data
            if "timestamp" not in df.columns or "entropy" not in df.columns:
                logging.error("CSV missing required columns: 'timestamp', 'entropy'. "
                              "Found columns: %s", df.columns.tolist())
                return

            # Convert timestamps if needed
            df["timestamp"] = pd.to_datetime(df["timestamp"])

            # Plot entropy over time
            plt.figure(figsize=(10, 6))
            plt.plot(df["timestamp"], df["entropy"], label="Entropy", color="purple")
            plt.xlabel("Time")
            plt.ylabel("Entropy")
            plt.title("Entropy Over Time")
            plt.legend()
            plt.tight_layout()

            # Save chart
            output_dir = "charts"
            os.makedirs(output_dir, exist_ok=True)
            chart_path = os.path.join(output_dir, "entropy_chart.png")
            plt.savefig(chart_path)
            plt.close()

            logging.info(f"[{self.agent_name}] Chart created at: {chart_path}")

        except Exception as e:
            logging.exception(f"Error creating chart: {e}")

    def update_site(self):
        """
        Placeholder function to illustrate how you'd trigger a Cloudflare or other
        deployment. This could involve calling an API, running a shell command,
        or using a CI/CD pipeline.
        """
        # Example pseudocode:
        # response = requests.post(
        #     "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache",
        #     headers={"Authorization": "Bearer XYZ"},
        #     json={"files": ["https://yourdomain.com/anything"]}
        # )
        # if response.status_code == 200:
        #     logging.info("Cloudflare cache purged successfully.")
        # else:
        #     logging.error("Failed to purge cache: %s", response.text)

        logging.info(f"[{self.agent_name}] (Simulation) Updating site via Cloudflare...")

        # For now, let's pretend it succeeded:
        success = True
        if success:
            logging.info(f"[{self.agent_name}] Site update completed successfully.")
        else:
            logging.error(f"[{self.agent_name}] Site update failed.")

    def summarize_recent_data(self, data_path: str = "data/simulation_output.csv"):
        """
        Generates a short text summary of the latest data. Could feed into a
        changelog, Slack notification, or webpage status.
        """
        try:
            if not os.path.exists(data_path):
                logging.error(f"Data file not found at: {data_path}")
                return

            df = pd.read_csv(data_path)
            if "entropy" not in df.columns or "complexity" not in df.columns:
                logging.error(
                    "CSV missing required columns for summary: 'entropy' or 'complexity'."
                )
                return

            # Let's assume the last row is the most recent
            latest = df.iloc[-1]
            summary = (
                f"As of {latest['timestamp']}, entropy is {latest['entropy']}, "
                f"and complexity is {latest['complexity']}. "
                "This might indicate a stable cluster, or the potential for a phase transition."
            )

            # Write to a simple text log with a timestamp
            os.makedirs("summaries", exist_ok=True)
            filename = datetime.utcnow().strftime("%Y%m%d_%H%M%S_summary.txt")
            summary_path = os.path.join("summaries", filename)

            with open(summary_path, "w") as f:
                f.write(summary)

            logging.info(
                f"[{self.agent_name}] Summary generated: {summary_path}"
            )
            logging.info(f"Summary contents: {summary}")

        except Exception as e:
            logging.exception(f"Error summarizing recent data: {e}")
