use telegram_bot::{
    UpdateKind,
    MessageKind,
    Error,
    CanReplySendMessage,
    Api,
};

use futures::StreamExt;

#[tokio::main]
async fn main() -> Result<(), Error> {

    let token = match dotenv::var("API_KEY") {
        Ok(value) => value,
        Err(_) => panic!("\x1b[31mPlease create .env file in project directory and put secret API key into variable `API_KEY`\x1b[0m"),
    };

    let bot = Api::new(token);

    // Fetch new updates via long poll method
    let mut stream = bot.stream();
    while let Some(update) = stream.next().await {
        // If the received update contains a new message...
        let update = update?;
        if let UpdateKind::Message(message) = update.kind {
            if let MessageKind::Text { ref data, .. } = message.kind {
                // Print received text message to stdout.
                println!("<{}>: {}", &message.from.first_name, data);

                bot.send(message.text_reply(format!(
                    "Hi, {}! You just wrote '{}'",
                    &message.from.first_name, data
                ))).await?;

            }
        }
    }
    Ok(())
}
