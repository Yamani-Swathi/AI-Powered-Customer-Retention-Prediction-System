import os
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


class EDA:

    def __init__(self):
        self.df = pd.read_csv(
            r"C:\Vihara_Tech\Churn_Prediction\Churn_Updated_set.csv"
        )

        # 📁 Folder to save all plots
        self.save_path = r"C:\Vihara_Tech\Churn_Prediction\Plots"
        os.makedirs(self.save_path, exist_ok=True)

        self.plot_no = 1  # counter for filenames

    # ---------- Save helper ----------
    def save_plot(self, name):
        filename = f"{self.plot_no:02d}_{name}.png"
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_path, filename))
        plt.close()
        self.plot_no += 1

    # ---------- Helper Functions ----------
    def bar_count_pct(self, count, pct, title, ylabel, fname):
        ax = count.plot(kind='bar')
        ax.set_title(title)
        ax.set_ylabel(ylabel)

        for i, p in enumerate(ax.patches):
            ax.annotate(
                f'{count.iloc[i]} ({pct.iloc[i]:.1f}%)',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom'
            )

        self.save_plot(fname)

    def bar_pct(self, data, title, fname):
        ax = data.plot(kind='bar')
        ax.set_title(title)
        ax.set_ylabel('Percentage')

        for p in ax.patches:
            ax.annotate(
                f'{p.get_height():.1f}%',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom'
            )

        self.save_plot(fname)

    def pie_pct(self, series, title, fname):
        pct = series.value_counts(normalize=True) * 100
        pct.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title(title)
        plt.ylabel('')
        self.save_plot(fname)

    def line_pct(self, table, title, fname):
        table.plot(marker='o')
        plt.title(title)
        plt.ylabel('Percentage')
        plt.xticks(rotation=45)
        plt.grid(True)
        self.save_plot(fname)

    # ---------- All Visualizations ----------
    def run_visualizations(self):

        # 1️⃣ Churn vs Non-Churn (Bar)
        count = self.df['Churn'].value_counts()
        pct = self.df['Churn'].value_counts(normalize=True) * 100
        self.bar_count_pct(
            count, pct,
            'Churn vs Non-Churn (Count & %)',
            'Customers',
            'churn_vs_nonchurn_bar'
        )

        # 2️⃣ Churn Distribution (Pie)
        self.pie_pct(
            self.df['Churn'],
            'Churn Distribution (%)',
            'churn_distribution_pie'
        )

        # 3️⃣ Gender-wise Churn
        churn = self.df[self.df['Churn'] == 'Yes']
        count = churn['gender'].value_counts()
        pct = churn['gender'].value_counts(normalize=True) * 100
        self.bar_count_pct(
            count, pct,
            'Gender-wise Churn (Count & %)',
            'Churn Count',
            'genderwise_churn'
        )

        # 4️⃣ Churn by Gender & Senior
        pct = pd.crosstab(churn['gender'], churn['SeniorCitizen'],
                          normalize='index') * 100
        pct.columns = ['Non-Senior', 'Senior']
        self.bar_pct(
            pct,
            'Churn by Gender & Senior Citizen (%)',
            'churn_gender_senior'
        )

        # 5️⃣ Internet Service by Gender
        pct = pd.crosstab(self.df['gender'], self.df['InternetService'],
                          normalize='index') * 100
        self.bar_pct(
            pct,
            'Internet Service by Gender (%)',
            'internet_by_gender'
        )

        # 6️⃣ Phone Service (Churned)
        churn['GS'] = churn['gender'] + '-' + churn['SeniorCitizen'].map(
            {0: 'Non-Senior', 1: 'Senior'}
        )
        pct = pd.crosstab(churn['GS'], churn['PhoneService'],
                          normalize='index') * 100
        self.bar_pct(
            pct,
            'Phone Service (Churned %)',
            'phone_service_churned'
        )

        # 7️⃣ Multiple Lines by Gender & Senior
        self.df['GS'] = self.df['gender'] + '-' + self.df['SeniorCitizen'].map(
            {0: 'Non-Senior', 1: 'Senior'}
        )
        pct = pd.crosstab(self.df['GS'], self.df['MultipleLines'],
                          normalize='index') * 100
        self.bar_pct(
            pct,
            'Multiple Lines by Gender & Senior (%)',
            'multiple_lines_gender_senior'
        )

        # 8️⃣ Multiple Lines by SIM
        pct = pd.crosstab(self.df['SIM_Provider'], self.df['MultipleLines'],
                          normalize='index') * 100
        self.bar_pct(
            pct,
            'Multiple Lines by SIM (%)',
            'multiple_lines_by_sim'
        )

        # 9️⃣ Multiple Lines by SIM & Gender
        self.df['SIM_G'] = self.df['SIM_Provider'] + '-' + self.df['gender']
        pct = pd.crosstab(self.df['SIM_G'], self.df['MultipleLines'],
                          normalize='index') * 100
        self.bar_pct(
            pct,
            'Multiple Lines by SIM & Gender (%)',
            'multiple_lines_sim_gender'
        )

        # 🔟 Multiple Lines Trend (Line)
        self.df['SGS'] = (
            self.df['SIM_Provider'] + '-' +
            self.df['gender'] + '-' +
            self.df['SeniorCitizen'].astype(str)
        )
        pct = pd.crosstab(self.df['SGS'], self.df['MultipleLines'],
                          normalize='index') * 100
        self.line_pct(
            pct,
            'Multiple Lines Trend (%)',
            'multiple_lines_trend'
        )

        # 11️⃣ Internet Service Distribution (Pie)
        self.pie_pct(
            self.df['InternetService'],
            'Internet Service Distribution (%)',
            'internet_service_distribution'
        )

        # 12️⃣ Internet Service by SIM
        pct = pd.crosstab(self.df['InternetService'], self.df['SIM_Provider'],
                          normalize='index') * 100
        self.bar_pct(
            pct,
            'Internet Service by SIM (%)',
            'internet_by_sim'
        )

        # 13️⃣ Internet by SIM & Gender
        pct = pd.crosstab(
            [self.df['SIM_Provider'], self.df['gender']],
            self.df['InternetService'],
            normalize='index'
        ) * 100
        self.bar_pct(
            pct,
            'Internet by SIM & Gender (%)',
            'internet_sim_gender'
        )

        # 14️⃣ Internet by SIM, Gender & Churn
        pct = pd.crosstab(
            [self.df['SIM_Provider'], self.df['gender']],
            self.df['Churn'],
            normalize='index'
        ) * 100
        self.bar_pct(
            pct,
            'Internet by SIM, Gender & Churn (%)',
            'internet_sim_gender_churn'
        )

        # 15️⃣ Service Distribution
        services = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                    'TechSupport', 'StreamingTV', 'StreamingMovies']
        for s in services:
            pct = self.df[s].value_counts(normalize=True) * 100
            self.bar_pct(
                pct,
                f'{s} Distribution (%)',
                f'{s.lower()}_distribution'
            )

        # 16️⃣ Contract Distribution
        pct = pd.crosstab(
            [self.df['SIM_Provider'], self.df['gender']],
            self.df['Contract'],
            normalize='index'
        ) * 100
        self.bar_pct(
            pct,
            'Contract Distribution (%)',
            'contract_distribution'
        )

        # 17️⃣ Contract by Gender, Senior & SIM
        self.df['GS_SIM'] = (
            self.df['gender'] + '-' +
            self.df['SeniorCitizen'].astype(str) + '-' +
            self.df['SIM_Provider']
        )
        pct = pd.crosstab(self.df['GS_SIM'], self.df['Contract'],
                          normalize='index') * 100
        self.bar_pct(
            pct,
            'Contract by Gender, Senior & SIM (%)',
            'contract_gender_senior_sim'
        )

        # 18️⃣ Paperless Billing
        pct = pd.crosstab(
            [self.df['SIM_Provider'], self.df['gender']],
            self.df['PaperlessBilling'],
            normalize='index'
        ) * 100
        self.bar_pct(
            pct,
            'Paperless Billing (%)',
            'paperless_billing'
        )

        # 19️⃣ Payment Method by Gender & Churn
        pct = pd.crosstab(
            [self.df['PaymentMethod'], self.df['gender']],
            self.df['Churn'],
            normalize='index'
        ) * 100
        self.bar_pct(
            pct,
            'Payment Method by Gender & Churn (%)',
            'payment_method_gender_churn'
        )


# ---------- Run ----------
eda = EDA()
eda.run_visualizations()

print("✅ All EDA plots saved successfully!")
