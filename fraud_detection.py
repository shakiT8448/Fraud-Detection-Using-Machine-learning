import streamlit 
import pandas 
import joblib
model = joblib.load("fraud_detection_pipeline.pkl")

streamlit.title("برنامه ی تشخیص کلاهبرداری")
streamlit.markdown("لطفا اطلاعات معامله را وارد کرده و سپس دکمه ی 'پیشبینی' را بزنید")
streamlit.markdown("""
<style>
body, html {
 
}
p, div, label, h1, h2, h3, h4, h5, h6 {
    direction: RTL;
}
input{
 dir=auto;
}
selectbox{
dir= ltr;}
</style>
""", unsafe_allow_html=True)
streamlit.divider()

transaction_type = streamlit.selectbox("نوع معامله", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = streamlit.number_input("وجه", min_value = 0, value = 10000)
oldbalanceOrg = streamlit.number_input("موجودی قدیمی حساب بانکی (حساب واریز کننده)", min_value = 0, value = 100000 )
newbalanceOrig = streamlit.number_input("موجودی جدید حساب بانکی (حساب واریز کننده)", min_value = 0, value = 10000 )
oldbalanceDest = streamlit.number_input("موجودی قدیمی حساب بانکی (حساب مقصد)", min_value = 0, value = 10000 )
newbalanceDest = streamlit.number_input("موجودی جدید حساب بانکی (حساب مقصد)", min_value = 0, value = 10000 )

if streamlit.button("پیشبینی"):
    input_data = pandas.DataFrame([{
        "type" : transaction_type,
        "amount" : amount,
        "oldbalanceOrg" : oldbalanceOrg,
        "newbalanceOrig" : newbalanceOrig,
        "oldbalanceDest" : oldbalanceDest,
        "newbalanceDest" : newbalanceDest
    }])
    prediction = model.predict(input_data)[0]
    streamlit.subheader(f"پیشبینی : '{int(prediction)}'")
    if prediction == 1:
        streamlit.error("احتمال کلاهبرداری بودن این جابه جایی بالا است")
    else:
        streamlit.success("احتمال کلاهبرداری بودن این جابه جایی بسیار کم است")
