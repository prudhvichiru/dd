const nodemailer = require('nodemailer');

module.exports = async (req, res) => {
  // Only allow POST
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { who, name, postcode, phone, email, when, story, updates } = req.body;

  // Basic validation
  if (!name || !phone) {
    return res.status(400).json({ error: 'Name and phone are required' });
  }

  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.GMAIL_USER,
      pass: process.env.GMAIL_PASS, // Gmail App Password
    },
  });

  const mailBody = `
New enquiry from Dementia Diagnostics website
================================================

Getting in touch : ${who || '-'}
Name             : ${name}
Postcode         : ${postcode || '-'}
Phone            : ${phone}
Email            : ${email || 'Not provided'}
Best time        : ${when || '-'}
Updates opt-in   : ${updates === 'on' ? 'Yes' : 'No'}

Message:
${story || 'Not provided'}
  `.trim();

  try {
    await transporter.sendMail({
      from: `"Dementia Diagnostics Website" <${process.env.GMAIL_USER}>`,
      to: 'rohit.bansal@dementiadiagnostics.com.au',
      replyTo: email || undefined,
      subject: `New Enquiry – ${name} (${postcode || 'no postcode'})`,
      text: mailBody,
    });

    return res.status(200).json({ success: true });
  } catch (err) {
    console.error('Mail error:', err);
    return res.status(500).json({ error: 'Failed to send email. Please try again.' });
  }
};
