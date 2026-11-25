"""Builds the Dementia Diagnostics multi-view site."""
import re, sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/55a0f5d5-6f3a-50d8-8b16-98f009e673a7/scratchpad')

# ---------------------------------------------------------------- brand assets
logo_src = open('logo_mark.svg', encoding='utf-8').read()
m = re.search(r'viewBox="([^"]+)".*?<g fill="currentColor" fill-rule="nonzero">(.*)</g></svg>', logo_src, re.S)
LOGO_VB, LOGO_INNER = m.group(1), m.group(2)

import art
ART_HERO, ART_FAM, ART_CLIN, ART_STEP = art.HERO, art.FAM, art.CLIN, art.STEP

LOGO = f'<svg class="logo" viewBox="{LOGO_VB}" role="img" aria-label="Dementia Diagnostics" ' \
       f'xmlns="http://www.w3.org/2000/svg"><g fill="currentColor" fill-rule="nonzero">{LOGO_INNER}</g></svg>'
LOGO_FOOT = LOGO.replace('class="logo"', 'class="logo logo-foot" aria-hidden="true" focusable="false"') \
                .replace(' role="img"', '').replace(' aria-label="Dementia Diagnostics"', '')

NAV = [("home", "Home"), ("assessment", "The assessment"), ("families", "Families & carers"),
       ("gps", "For GPs"), ("clinicians", "Our clinicians")]

# ---------------------------------------------------------------- views
HOME = f'''
<section class="band hero">
  <div class="inner">
    <div class="hero-grid">
      <div class="hero-copy">
        <p class="eyebrow">A virtual memory clinic for regional Australia</p>
        <h1>Something has changed.<br><em>You don't have to work it out alone.</em></h1>
        <p class="lede">If you or someone you love has been forgetting things, we can help you find out
          what's going on. A specialist, from home, without the long drive or the long wait.</p>
        <div class="cta-row">
          <a class="btn" href="#home" data-scroll="enquiry">Talk to us</a>
          <a class="btn ghost" href="#gps">I'm a GP</a>
        </div>
        <p class="notice"><b>Video consultations begin mid-2027.</b> We're taking enquiries now,
          on the Gold Coast and in South Brisbane first. Register your interest and we'll call you
          to talk it through, and again as soon as appointments open.</p>
        <p class="reassure">Nothing is booked, and nothing happens, until you say so.</p>
      </div>
      <figure class="shot shot-sq">{ART_HERO}</figure>
    </div>
  </div>
</section>

<section class="band cool">
  <div class="inner">
    <h2>Does any of this sound <em>familiar?</em></h2>
    <div class="cards">
      <div class="card">The same question, three times in one afternoon.</div>
      <div class="card">A road she's driven for thirty years, and this time she wasn't sure.</div>
      <div class="card">Bills that always got paid, starting to pile up.</div>
      <div class="card">You mentioned it to the GP once. It didn't really go anywhere.</div>
      <div class="card">Your brother thinks it's just getting older. You're not so sure.</div>
      <div class="card">You've been meaning to do something about it for a while now.</div>
    </div>
    <p class="after-cards">None of these mean it's dementia. <b>All of them are worth looking at
      properly.</b> Memory changes have many causes, and some of them are treatable.</p>
  </div>
</section>

<section class="band">
  <div class="inner">
    <h2>The hardest part is usually <em>the waiting</em></h2>
    <p class="lede" style="margin-top:1rem">In Australia, the gap between first noticing something and
      getting an answer is about three years. If you live outside a capital city, it is often longer.</p>
    <div class="stats">
      <div class="stat"><div class="fig">~3 years</div>
        <p>Typical gap between first symptoms and a diagnosis. Closer to five for younger-onset dementia.</p></div>
      <div class="stat"><div class="fig">1 in 3</div>
        <p>People living with dementia in Australia are in regional or remote areas.</p></div>
      <div class="stat"><div class="fig">14 of 18</div>
        <p>Public memory clinics in NSW are in metropolitan Sydney.</p></div>
    </div>
    <p class="src">Figures from the National Dementia Action Plan 2024 to 2034 and the Australian Institute
      of Health and Welfare. We'd rather show you the real numbers than tell you it's fine.</p>
  </div>
</section>

<section class="band cool">
  <div class="inner">
    <h2>How it works</h2>
    <p class="lede" style="margin-top:1rem">Four steps, and a person with you at every one.</p>
    <div class="steps">
      <div class="step"><div class="n" aria-hidden="true"></div><div>
        <h3>You tell us what you've noticed</h3>
        <p>A phone or video conversation with one of our nurses, about twenty minutes. No tests.</p></div></div>
      <div class="step"><div class="n" aria-hidden="true"></div><div>
        <h3>We gather the background</h3>
        <p>With your permission we collect what your GP and others already hold.</p></div></div>
      <div class="step"><div class="n" aria-hidden="true"></div><div>
        <h3>You see a specialist, from your kitchen table</h3>
        <p>A geriatrician or old-age psychiatrist, by video, with family welcome.
          Video consultations begin mid-2027.</p></div></div>
      <div class="step"><div class="n" aria-hidden="true"></div><div>
        <h3>You get a plan, and so does your GP</h3>
        <p>Written in plain language, with a clear next step.</p></div></div>
    </div>
    <p style="margin-top:2rem"><a class="btn ghost" href="#assessment">What happens at an assessment</a></p>
  </div>
</section>

<section class="band warm">
  <div class="inner">
    <div class="split">
      <figure class="shot shot-wide">{ART_FAM}</figure>
      <div>
        <h2>If you're reading this <em>for someone else</em></h2>
        <p style="margin-top:1rem">A lot of people who come to us weren't the one who noticed first.
          A daughter rang. A husband finally said something out loud. A neighbour mentioned it.</p>
        <p style="margin-top:0.9rem">You can start the conversation without committing anyone to anything.
          If raising it is the hard part, our nurses do this every day.</p>
        <p style="margin-top:1.4rem"><a class="btn ghost" href="#families">For families and carers</a></p>
      </div>
    </div>
  </div>
</section>

{{ENQUIRY}}
'''

ASSESSMENT = f'''
<section class="band">
  <div class="inner">
    <p class="eyebrow">The assessment</p>
    <h1 class="page-title">What actually <em>happens</em></h1>
    <p class="lede" style="margin-top:1rem">From the first phone call to the letter that reaches your GP,
      here is the whole thing, step by step. It takes a few weeks, not a few years.</p>
  </div>
</section>

<section class="band cool">
  <div class="inner">
    <div class="split">
      <div>
        <h2>Step one: <em>the first call</em></h2>
        <p style="margin-top:1rem">One of our nurses rings you. It takes about twenty minutes and there is
          no test in it. They'll ask what you've noticed, when it started, and how it's affecting ordinary
          days. If someone else noticed first, they're welcome on the call.</p>
        <p style="margin-top:0.9rem">At the end of it you'll know whether an assessment makes sense, what it
          will involve, and what it will cost. If it isn't right for you, we'll say so and point you
          somewhere better.</p>
      </div>
      <figure class="shot shot-step">{ART_STEP}</figure>
    </div>
  </div>
</section>

<section class="band">
  <div class="inner">
    <h2>Step two: <em>gathering the background</em></h2>
    <p class="lede" style="margin-top:1rem">This is the part that usually takes months. We do it for you.</p>
    <div class="qa">
      <div><h3>What we collect</h3>
        <p>Your GP's records, past test results, your medication list, and anything from other specialists
          you've seen. We ask your permission for each source.</p></div>
      <div><h3>What we ask you for</h3>
        <p>A short questionnaire about daily life, and the same one for a family member if you have one.
          Both matter, and they often say slightly different things.</p></div>
      <div><h3>Tests before the appointment</h3>
        <p>Usually blood tests at your local collection centre, and sometimes a scan. We arrange the
          referrals so you don't have to chase them.</p></div>
      <div><h3>Thinking and memory tests</h3>
        <p>Done with a clinician guiding you, not alone with a screen. There's nothing to revise for and
          nothing to fail.</p></div>
    </div>
  </div>
</section>

<section class="band cool">
  <div class="inner">
    <h2>Step three: <em>the consultation</em></h2>
    <p class="notice" style="margin-top:1rem"><b>Available from mid-2027.</b> Video consultations
      are not running yet. Everything on this page describes the service as it will operate when
      appointments open.</p>
    <div class="twoup">
      <div>
        <p>Around an hour by video with a geriatrician or old-age psychiatrist. Longer than most specialist
          appointments, because the history is the diagnosis.</p>
        <p>Family are welcome, in the room with you or dialling in from somewhere else. If you'd rather
          part of the conversation happened without them, say so and we'll arrange it.</p>
      </div>
      <div>
        <p><b>What you need:</b> a device with a camera, somewhere quiet, and about 60 minutes free.
          If the technology is the obstacle, tell us and we'll sort it out before the day.</p>
        <p><b>If video won't work at all,</b> tell us that too. We'll find another way rather than
          letting it stop the assessment.</p>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="inner">
    <h2>Step four: <em>what you get</em></h2>
    <div class="cards">
      <div class="card"><b>An explanation</b><br>In plain language, in the appointment, with time to ask
        everything twice if you want to.</div>
      <div class="card"><b>A written summary</b><br>Yours to keep, to read again later, and to show
        whoever else needs to see it.</div>
      <div class="card"><b>A plan</b><br>What happens next, who does it, and when. Including the things
        that aren't medical.</div>
      <div class="card"><b>A letter to your GP</b><br>Structured and specific, so your own doctor can act
        on it straight away.</div>
      <div class="card"><b>A review</b><br>Memory changes over time. We'll tell you when to come back and
        what would bring that forward.</div>
      <div class="card"><b>Somewhere to call</b><br>Questions don't arrive on schedule. You can ring us
        after the appointment.</div>
    </div>
  </div>
</section>

<section class="band warm">
  <div class="inner">
    <h2>The things people <em>actually</em> worry about</h2>
    <div class="qa">
      <div><h3>What if it turns out to be nothing?</h3>
        <p>Then you'll know, and you can stop carrying it around. That is a good outcome, not a wasted
          appointment.</p></div>
      <div><h3>What if it turns out to be something?</h3>
        <p>Then you've found out sooner, which means more time to plan, more options, and more say in what
          happens. People tell us the not knowing was the worst part.</p></div>
      <div><h3>Can I fail this?</h3>
        <p>No. It isn't an exam and there's nothing to revise for. It's a conversation and some structured
          questions, with a specialist who does this all day.</p></div>
      <div><h3>Does it have to mean dementia?</h3>
        <p>No. Thyroid problems, medications, depression, hearing loss, vitamin deficiency and sleep can all
          affect memory, and several of those are fixable.</p></div>
      <div><h3>What will it cost?</h3>
        <p>Most assessments attract a Medicare rebate. We'll tell you exactly what you'll pay before
          anything is booked. No surprises, and no obligation to continue.</p></div>
      <div><h3>Do I need a GP referral?</h3>
        <p>It helps, and it's usually needed for the Medicare rebate. Get in touch first if you'd rather,
          and we'll talk you through it.</p></div>
    </div>
    <p style="margin-top:2.2rem"><a class="btn" href="#home" data-scroll="enquiry">Talk to us</a></p>
  </div>
</section>
'''

FAMILIES = f'''
<section class="band">
  <div class="inner">
    <div class="split">
      <div>
        <p class="eyebrow">Families and carers</p>
        <h1 class="page-title">You noticed. <em>That counts.</em></h1>
        <p class="lede" style="margin-top:1rem">Most people who reach us were brought here by someone else.
          A daughter rang. A husband finally said it out loud. A neighbour mentioned it to the GP.</p>
      </div>
      <figure class="shot shot-wide">{ART_FAM}</figure>
    </div>
  </div>
</section>

<section class="band cool">
  <div class="inner">
    <h2>Raising it is the <em>hardest part</em></h2>
    <p class="lede" style="margin-top:1rem">Not the appointment. The conversation before it.</p>
    <div class="qa">
      <div><h3>Start with what you saw, not what you think it means</h3>
        <p>"You asked me about Tuesday three times yesterday" lands very differently from "I think
          something's wrong with your memory."</p></div>
      <div><h3>Pick a calm moment, not a bad one</h3>
        <p>Straight after a mistake is the worst time. The conversation goes better when nobody is already
          embarrassed.</p></div>
      <div><h3>Name the fear rather than stepping around it</h3>
        <p>Most people have already thought about it and are frightened. Saying so out loud is usually a
          relief rather than a shock.</p></div>
      <div><h3>Offer the ordinary version</h3>
        <p>"Let's just get it checked, the way you'd get a sore knee looked at." Many causes of memory
          change are treatable, and that's a true and useful thing to say.</p></div>
      <div><h3>You don't have to win it the first time</h3>
        <p>Plant it, leave it, come back. Pushing hard on day one often sets things back.</p></div>
      <div><h3>You can ring us first</h3>
        <p>Before you say anything to them. Our nurses have this conversation most days and will talk it
          through with you.</p></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="inner">
    <h2>What you've seen <em>matters clinically</em></h2>
    <div class="twoup">
      <div>
        <p>Diagnosis leans heavily on how someone is managing day to day, and the person themselves often
          can't see the change, or plays it down without meaning to.</p>
        <p>The detail of what altered, when, and what they can still do is some of the most useful
          information a specialist gets. You're not telling tales. You're part of the assessment.</p>
      </div>
      <div>
        <p><b>Useful things to jot down:</b> when you first noticed. What specifically changed. What they
          managed a year ago that's harder now. Whether it's getting worse steadily or coming and going.
          Any falls, any new medicines.</p>
        <p><b>You'll be asked to complete a short questionnaire</b> about daily function. Answer it
          honestly rather than kindly. Kind answers make the picture less clear.</p>
      </div>
    </div>
  </div>
</section>

<section class="band warm">
  <div class="inner">
    <h2>Some particular <em>situations</em></h2>
    <div class="qa">
      <div><h3>They live alone</h3>
        <p>Tell us. We'll handle appointment reminders, setting up the video call and the practical parts,
          rather than leaving them to you or to chance.</p></div>
      <div><h3>You live interstate</h3>
        <p>You can join the consultation by video from wherever you are. Plenty of families do the whole
          thing from three different postcodes.</p></div>
      <div><h3>You're a younger carer</h3>
        <p>Adult children often end up coordinating appointments and medications long before anyone calls
          them a carer. Say so, and we'll copy you in properly rather than by accident.</p></div>
      <div><h3>They don't want you involved</h3>
        <p>That's their right, and we'll respect it. We can still hear from you; we just may not be able to
          tell you everything back. We'll always be straight with you about which it is.</p></div>
      <div><h3>You disagree with your siblings</h3>
        <p>Extremely common, and not a reason to wait. An assessment replaces the argument with something
          factual.</p></div>
      <div><h3>You're exhausted</h3>
        <p>Dementia Australia's National Dementia Helpline is on 1800 100 500, any time, for support that
          isn't about appointments.</p></div>
    </div>
    <p style="margin-top:2.2rem"><a class="btn" href="#home" data-scroll="enquiry">Talk to us</a></p>
  </div>
</section>
'''

GPS = '''
<section class="band">
  <div class="inner">
    <p class="eyebrow">For referring GPs</p>
    <h1 class="page-title">Your patient, <em>back in your care</em></h1>
    <p class="lede" style="margin-top:1rem">We're a specialist assessment service, not a replacement for the
      relationship you already have. We take the work-up off your plate and send you something you can act on.</p>
  </div>
</section>

<section class="band cool">
  <div class="inner">
    <h2>What we take on</h2>
    <div class="qa">
      <div><h3>Case preparation</h3>
        <p>We collect prior records, correspondence and results, and chase what's missing. Your practice
          sends the referral and nothing else.</p></div>
      <div><h3>Collateral history</h3>
        <p>Structured informant history from family, captured properly rather than squeezed into a
          consultation.</p></div>
      <div><h3>Cognitive assessment</h3>
        <p>Administered by a clinician, with the instrument chosen for the patient rather than for
          convenience. Scores returned as data, not a screenshot.</p></div>
      <div><h3>Specialist consultation</h3>
        <p>A geriatrician or old-age psychiatrist, by video, with a full hour.</p></div>
      <div><h3>The difficult conversation</h3>
        <p>Diagnosis is disclosed by the specialist, with family present, and with time for it.</p></div>
      <div><h3>A plan you can run</h3>
        <p>Specific recommendations with who does what, written to be actionable in general practice.</p></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="inner">
    <h2>How referrals <em>reach us</em></h2>
    <div class="twoup">
      <div>
        <p><b>Through Medical-Objects</b>, into and out of Best Practice and Medical Director. If you
          already send specialist referrals electronically, this works the same way.</p>
        <p>We write back through the same channel, so the report lands in your inbox rather than in a
          patient's handbag.</p>
      </div>
      <div>
        <p><b>Useful to include:</b> what prompted the referral, current medications, recent bloods, any
          imaging, and who in the family is involved.</p>
        <p><b>Not required:</b> a completed cognitive screen. If you've done one we'll use it; if you
          haven't, that's not a reason to delay the referral.</p>
      </div>
    </div>
  </div>
</section>

<section class="band cool">
  <div class="inner">
    <h2>Who we're <em>right for</em></h2>
    <div class="twoup">
      <div>
        <p><b>Well suited:</b> adults with memory or cognitive concerns where a specialist opinion would
          help, particularly where travelling to a metropolitan memory clinic is the barrier.</p>
      </div>
      <div>
        <p><b>Not suited:</b> acute confusion or suspected delirium, acute psychiatric presentations, and
          anyone who needs to be seen today. Those need your usual urgent pathways, not a booked
          telehealth assessment.</p>
      </div>
    </div>
    <p class="notice" style="margin-top:2rem"><b>We begin accepting referrals in mid-2027</b>,
      on the Gold Coast and in South Brisbane first. We'd still like to hear from you before then:
      the referral pathway and the report format are being designed with GPs now.</p>
    <p style="margin-top:2.2rem"><a class="btn" href="#home" data-scroll="enquiry">Get in touch about referring</a></p>
  </div>
</section>
'''

CLINICIANS = f'''
<section class="band">
  <div class="inner">
    <div class="split">
      <div>
        <p class="eyebrow">Our clinicians</p>
        <h1 class="page-title">Who you'll <em>actually see</em></h1>
        <p class="lede" style="margin-top:1rem">Not a call centre, and not software. A named specialist who
          sees you for a full hour and whose name is on the letter that goes back to your GP.</p>
      </div>
      <figure class="shot shot-wide">{ART_CLIN}</figure>
    </div>
  </div>
</section>

<section class="band cool">
  <div class="inner">
    <h2>The team around an assessment</h2>
    <div class="qa">
      <div><h3>A nurse</h3>
        <p>Your first call and your point of contact throughout. They gather the history, arrange the tests
          and make sure the technology works before the day.</p></div>
      <div><h3>A geriatrician or old-age psychiatrist</h3>
        <p>The specialist who assesses you, reaches the diagnosis and explains it. A geriatrician for most
          people; an old-age psychiatrist where mood, behaviour or psychiatric history is prominent.</p></div>
      <div><h3>A pharmacist, where medications are part of the picture</h3>
        <p>Polypharmacy is one of the genuinely treatable contributors to memory change in older people,
          and it is easy to miss in a short appointment.</p></div>
      <div><h3>Your own GP</h3>
        <p>Not an afterthought. They keep the relationship and the ongoing care, and we write to them
          properly.</p></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="inner">
    <h2>What we hold <em>ourselves to</em></h2>
    <div class="cards">
      <div class="card"><b>Registered, every one</b><br>Every clinician is registered with Ahpra and
        practises within their scope. You can check any of them on the public register.</div>
      <div class="card"><b>A full hour</b><br>Cognitive assessment done briefly is cognitive assessment
        done badly. The history is the diagnosis and it takes as long as it takes.</div>
      <div class="card"><b>Continuity</b><br>The same specialist follows you through the assessment and
        the review. You won't re-tell your story to a new face.</div>
      <div class="card"><b>A clinician decides</b><br>We use software to prepare and organise information.
        Assessment and diagnosis are made by a person, every time.</div>
      <div class="card"><b>We say when we're not the answer</b><br>If you'd be better served somewhere
        else, we'll tell you at the first call rather than at the end.</div>
      <div class="card"><b>We write things down</b><br>You get the summary. Your GP gets the letter.
        Nothing important lives only in someone's memory of the conversation.</div>
    </div>
    <p style="margin-top:2.2rem"><a class="btn" href="#home" data-scroll="enquiry">Talk to us</a></p>
  </div>
</section>
'''

PRIVACY = '''
<section class="band">
  <div class="inner">
    <p class="eyebrow">Privacy</p>
    <h1 class="page-title">What we do with <em>your information</em></h1>
    <p class="lede" style="margin-top:1rem">Health information is sensitive, and we treat it that way.
      Here is what we collect, why, and who sees it.</p>
  </div>
</section>

<section class="band cool">
  <div class="inner">
    <div class="policy">
      <div><h3>What we collect</h3>
        <p>Your name and contact details. What you tell us about memory, thinking or daily life. Health
          information from your GP and others, where you have agreed to us collecting it. The records of
          your assessment, including notes, scores and correspondence.</p></div>
      <div><h3>Why we collect it</h3>
        <p>To assess you, to plan your care, and to write back to your GP. We also keep records because
          registered health practitioners are legally required to.</p></div>
      <div><h3>Who sees it</h3>
        <p>The clinicians and staff involved in your care, and your GP where you have agreed. Nobody else,
          unless you ask us to share it or the law requires it. We do not sell your information and we do
          not use your health information for marketing.</p></div>
      <div><h3>Two separate consents</h3>
        <p>Agreeing to be assessed and agreeing to hear from us about the clinic are different things. You
          can say yes to one and no to the other, and you can change your mind about either at any time
          without it affecting your care.</p></div>
      <div><h3>Where it is kept</h3>
        <p>In secure systems hosted in Australia. Access is limited to the people involved in your care,
          and every time your record is opened it is logged. Some cognitive tests run on platforms operated
          overseas. Where that applies to you, we will tell you before your assessment and you can
          decline.</p></div>
      <div><h3>How long we keep it</h3>
        <p>Clinical records are kept for at least seven years after your last appointment, and for a person
          under 18 until they turn 25. That is the legal requirement for health records in Australia.</p></div>
      <div><h3>Seeing and correcting your record</h3>
        <p>You can ask for a copy of what we hold about you, and you can ask us to correct anything that is
          wrong. Ask any member of our team and we will tell you how.</p></div>
      <div><h3>If you are unhappy</h3>
        <p>Tell us first and we will look into it. If you are not satisfied with how we handle it, you can
          complain to the Office of the Australian Information Commissioner at oaic.gov.au.</p></div>
    </div>
    <p class="draftnote" style="margin-top:2rem"><b>Draft.</b> This summary is written in plain language so
      it is actually read. It is being reviewed by our lawyers before launch, and the full policy will
      replace it here.</p>
  </div>
</section>
'''

ENQUIRY = '''
<section class="band cool" id="enquiry">
  <div class="inner">
    <h2>Start a <em>conversation</em></h2>
    <div class="form-wrap">
      <div>
        <p style="margin-top:0.8rem">Tell us a little and we'll call you back within one business day.
          There's no cost for this call, and no obligation at the end of it.</p>
        <p class="notice" style="margin-top:1.2rem"><b>Video consultations begin mid-2027.</b>
          Getting in touch now puts you on the list and starts the conversation. It does not book
          an appointment, because we are not seeing patients yet.</p>
        <p style="margin-top:1rem" class="hint">We're opening first on the Gold Coast and in South Brisbane,
          and adding regions after that. If you're somewhere else, still get in touch and we'll tell you
          honestly where we're up to.</p>
        <p class="urgent" style="margin-top:1.6rem">If you're worried about someone's immediate safety,
          please contact your GP, or call 000 in an emergency. This form isn't monitored around the clock.</p>
      </div>
      <div>
        <form id="enquiry-form" novalidate>
          <div class="field"><label for="who">I'm getting in touch</label>
            <select id="who" name="who">
              <option>About myself</option><option>About a parent or family member</option>
              <option>About someone I care for</option><option>As a health professional</option>
            </select></div>
          <div class="row2">
            <div class="field"><label for="name">Your first name</label>
              <input type="text" id="name" name="name" autocomplete="given-name"></div>
            <div class="field"><label for="postcode">Postcode</label>
              <input type="text" id="postcode" name="postcode" inputmode="numeric" autocomplete="postal-code"></div>
          </div>
          <div class="row2">
            <div class="field"><label for="phone">Phone</label>
              <input type="tel" id="phone" name="phone" autocomplete="tel"></div>
            <div class="field"><label for="email">Email <span class="hint">(optional)</span></label>
              <input type="email" id="email" name="email" autocomplete="email"></div>
          </div>
          <div class="field"><label for="when">Best time to reach you</label>
            <select id="when" name="when">
              <option>Any time during business hours</option><option>Morning</option>
              <option>Afternoon</option><option>Please email me instead</option>
            </select></div>
          <div class="field"><label for="story">What's prompted you to get in touch?
            <span class="hint">Optional, a sentence is plenty</span></label>
            <textarea id="story" name="story" placeholder="Whatever you'd like us to know before we call."></textarea></div>
          <div class="consent"><input type="checkbox" id="updates" name="updates">
            <label for="updates" style="font-weight:400">Separately, I'd like occasional updates about the
              clinic as it opens in new areas. <span class="hint">You can say no to this and still hear back
              about your enquiry.</span></label></div>
          <div><button class="btn" type="submit">Send</button></div>
          <p class="hint" style="max-width:52ch">We use what you tell us to respond to this enquiry.
            We don't sell it, and we don't share it without your consent.</p>
        </form>
        <div class="sent" id="sent" hidden>
          <h3>Thank you. That's all we need for now</h3>
          <p>One of our nurses will call you within one business day. If it's easier to talk at a different
            time, just tell them when you pick up.</p>
          <p style="margin-top:0.8rem">If anything changes before then, or you're worried about someone's
            safety, contact your GP or call 000.</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''

VIEWS = {'home': HOME.replace('{ENQUIRY}', ENQUIRY), 'assessment': ASSESSMENT, 'families': FAMILIES,
         'gps': GPS, 'clinicians': CLINICIANS, 'privacy': PRIVACY}
TITLES = {'home': 'Dementia Diagnostics', 'assessment': 'The assessment', 'families': 'Families and carers',
          'gps': 'For GPs', 'clinicians': 'Our clinicians', 'privacy': 'Privacy'}

views_html = "".join(
    f'<div class="view" id="view-{k}" hidden>{v}</div>' for k, v in VIEWS.items())
nav_html = "".join(f'<a href="#{k}" data-nav="{k}">{label}</a>' for k, label in NAV)

CSS = open('site.css', encoding='utf-8').read()
JS = open('site.js', encoding='utf-8').read()

html = f'''<title>Dementia Diagnostics</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,300..900;1,300..900&display=swap">
<style>{CSS}</style>

<header class="site-header">
  <div class="inner">
    <a class="brand" href="#home" aria-label="Dementia Diagnostics, home">{LOGO}</a>
    <nav class="mainnav" aria-label="Main">{nav_html}</nav>
  </div>
</header>

{views_html}

<footer>
  <div class="inner">
    {LOGO_FOOT}
    <p><b>Dementia Diagnostics Pty Ltd</b> &middot; ABN 18 700 637 270. A clinical service delivered by
      registered health practitioners: geriatricians, old-age psychiatrists and nurses, using secure video
      consultation. Assessment and diagnosis are carried out by a clinician, not by software.</p>
    <p>If you are worried about someone's immediate safety, contact your GP or call 000. For information and
      support at any time, Dementia Australia's National Dementia Helpline is available on 1800 100 500.</p>
    <nav class="footnav" aria-label="Footer">
      <a href="#home">Home</a><a href="#assessment">The assessment</a><a href="#families">Families &amp; carers</a>
      <a href="#gps">For GPs</a><a href="#clinicians">Our clinicians</a><a href="#privacy">Privacy</a>
    </nav>
  </div>
</footer>

<script>{JS}
window.DD_TITLES = {TITLES!r};
ddInit();
</script>
'''
open('dd-landing.html', 'w', encoding='utf-8').write(html)
print('built', len(html), 'bytes')
