import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import { ArrowDown, ArrowUpRight, Check, Cloud, GitBranch, Mail, Network, Phone, ShieldCheck, Terminal } from "lucide-react";
import { MorphIcon } from "morphicons/react";
import { ArrowDown as ArrowDownData, ArrowUpRight as ArrowUpRightData, Check as CheckData } from "lucide";
import ClickSpark from "./components/ClickSpark";
import "./styles.css";

const academicRecords = [
  { label: "CGPA", value: "3.79", detail: "Bachelor of IT (Hons.) Security Technology", evidence: "Transcript available on request", href: "mailto:chunhao021223@icloud.com?subject=Academic%20transcript%20request" },
  { label: "Dean's List", value: "2x", detail: "March + October session 2025", evidence: "Verification available on request", href: "mailto:chunhao021223@icloud.com?subject=Dean%27s%20List%20verification%20request" },
  { label: "MUET Band", value: "4.0", detail: "CEFR B2", evidence: "Verification available on request", href: "mailto:chunhao021223@icloud.com?subject=MUET%20result%20verification%20request" },
];

const labs = [
  { id: "assessment", number: "01", title: "Vulnerability Assessment", summary: "Reconnaissance, weakness validation, risk rating, and remediation reasoning.", evidence: "Academic practice and method notes" },
  { id: "cloud", number: "02", title: "Cloud Security Baseline", summary: "Identity, storage, network exposure, logging, and least-privilege review.", evidence: "Control checklist and learning reflections" },
  { id: "malware", number: "03", title: "Malware Behavior Analysis", summary: "Suspicious behavior, indicators, persistence ideas, and defensive signals.", evidence: "Structured observation notes" },
];

const experienceGroups = [
  { label: "Professional Experience", entries: [
    { period: "2023 - 2024", location: "Singapore", role: "IT Support", detail: "Technical troubleshooting, device readiness, and day-to-day user support." },
    { period: "2022 - 2023", location: "Singapore", role: "Administrative Assistant", detail: "Operational coordination, documentation, and accurate communication." },
  ] },
  { label: "University & Community", entries: [
    { period: "Campus", location: "MMU", role: "IT Club and Dragon Boat Club", detail: "Technical community participation alongside team discipline and training." },
  ] },
  { label: "Competitions & Events", entries: [
    { period: "2025", location: "Malaysia", role: "PROSOLVE National", detail: "Participant in a national problem-solving competition." },
    { period: "Volunteer", location: "Event support", role: "Infineon Interview Event", detail: "Supported participant flow and professional event coordination." },
  ] },
  { label: "Security Development", entries: [
    { period: "Training", location: "Security course project", role: "CEH v13 Preparation", detail: "Offensive security methodology and exam-oriented practice." },
  ] },
];

function scrollToId(event, id) {
  event.preventDefault();
  const target = document.getElementById(id);
  if (!target) return;
  window.history.replaceState(null, "", `#${id}`);
  target.scrollIntoView({ behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" });
}

function Reveal({ children, className = "" }) {
  return <div className={`reveal ${className}`}>{children}</div>;
}

function App() {
  const [activeLab, setActiveLab] = useState(labs[0].id);
  const [resumeRequested, setResumeRequested] = useState(false);

  useEffect(() => {
    const revealElements = document.querySelectorAll(".reveal");
    if (!("IntersectionObserver" in window)) {
      revealElements.forEach((element) => element.classList.add("is-visible"));
      return undefined;
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    revealElements.forEach((element) => observer.observe(element));
    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    if (!resumeRequested) return undefined;
    const reset = window.setTimeout(() => setResumeRequested(false), 1600);
    return () => window.clearTimeout(reset);
  }, [resumeRequested]);

  return (
    <>
      <ClickSpark />
      <div className="site-shell">
      <a className="skip-link" href="#main-content">Skip to main content</a>
      <header className="site-header">
        <nav className="nav container" aria-label="Portfolio navigation">
          <a className="brand" href="#top" onClick={(event) => scrollToId(event, "top")} aria-label="Back to top">LCH</a>
          <div className="nav-links">
            <a href="#academic" onClick={(event) => scrollToId(event, "academic")}>Academic</a>
            <a href="#experience" onClick={(event) => scrollToId(event, "experience")}>Experience</a>
            <a href="#contact" onClick={(event) => scrollToId(event, "contact")}>Contact</a>
          </div>
          <a className="nav-resume" href="/Liang-Chun-Hao-Resume.pdf" download onClick={() => setResumeRequested(true)}><span>Download resume</span><MorphIcon className="morph-icon" icon={resumeRequested ? CheckData : ArrowDownData} size={15} strokeWidth={1.5} reducedMotion="user" aria-hidden="true" /></a>
        </nav>
      </header>

      <main id="main-content">
        <section id="top" className="hero section container">
          <Reveal className="hero-name-wrap">
            <p className="section-kicker">Security Technology Portfolio</p>
            <h1>LIANG CHUN HAO</h1>
          </Reveal>

          <div className="hero-layout">
            <Reveal className="portrait-column">
              <figure className="portrait-frame">
                <img src="/avatar.jpg" alt="Liang Chun Hao" />
                <figcaption><span className="status-dot" /> Open to internship opportunities</figcaption>
              </figure>
              <a className="button button-dark" href="/Liang-Chun-Hao-Resume.pdf" download onClick={() => setResumeRequested(true)}>Download resume <MorphIcon className="morph-icon" icon={resumeRequested ? CheckData : ArrowDownData} size={15} strokeWidth={1.5} reducedMotion="user" aria-hidden="true" /></a>
            </Reveal>

            <div className="hero-right">
              <Reveal className="hero-copy">
                <p className="hero-index">01 / INTRODUCTION</p>
                <h2>Offensive curiosity.<br />Defensive discipline.</h2>
                <p className="hero-description">IT Security student building a practical foundation in testing, analysis, cryptography, secure systems, cloud controls, and cybersecurity law.</p>
                <p className="hero-focus">Pentesting <span>·</span> Cloud Security <span>·</span> Network Security</p>
                <a className="text-link" href="#labs" onClick={(event) => scrollToId(event, "labs")}>Explore learning labs <ArrowUpRight aria-hidden="true" /></a>
              </Reveal>

              <Reveal className="hero-cards" aria-label="Portfolio highlights">
                <article className="hero-card hero-card-dark">
                  <p className="card-label">Current focus</p>
                  <ul className="focus-list"><li><Terminal aria-hidden="true" /> Pentesting</li><li><Cloud aria-hidden="true" /> Cloud Security</li><li><Network aria-hidden="true" /> Network Security</li></ul>
                </article>
                <article className="hero-card">
                  <p className="card-label">Availability</p>
                  <p className="availability"><span className="status-dot" /> Open to internship opportunities</p>
                  <p className="card-note">Seeking a 2026 placement where careful technical learning and clear documentation matter.</p>
                </article>
                <a className="hero-card academic-snapshot" href="#academic" onClick={(event) => scrollToId(event, "academic")}>
                  <p className="card-label">Academic snapshot</p><strong>CGPA 3.79 <span>·</span> Dean&apos;s List 2x</strong><span className="card-action">View academic proof <ArrowUpRight aria-hidden="true" /></span>
                </a>
              </Reveal>
            </div>
          </div>
        </section>

        <section id="academic" className="section academic-section container">
          <Reveal><div className="academic-panel">
            <div className="panel-heading"><div><p className="section-kicker section-kicker-inverse">Academic proof</p><h2>Evidence of progress.</h2></div><ShieldCheck aria-hidden="true" /></div>
            <div className="academic-grid">{academicRecords.map((record) => (
              <a className="academic-record" href={record.href} key={record.label}><span>{record.label}</span><strong>{record.value}</strong><p>{record.detail}</p><em>{record.evidence}</em><ArrowUpRight aria-hidden="true" /></a>
            ))}</div>
            <div className="skill-row" aria-label="Relevant academic areas"><span>Ethical Hacking</span><span>Applied Cryptography</span><span>Digital Forensics</span></div>
          </div></Reveal>
        </section>

        <section id="labs" className="section labs-section container">
          <Reveal className="labs-feature">
            <figure className="labs-video">
              <video autoPlay muted loop playsInline preload="metadata" poster="https://i.pinimg.com/736x/ef/bf/54/efbf5402a4a1b221c21c41352b60056a.jpg" aria-label="Looping reference video">
                <source src="https://v1.pinimg.com/videos/mc/720p/58/52/22/58522209a4dea8dc8112185ad7efe70d.mp4" type="video/mp4" />
              </video>
            </figure>
            <div className="labs-feature-copy"><p className="section-kicker accent-kicker">What I build</p><h2>Security learning labs.</h2><p>Hands-on environments and writeups that shape thinking around offensive testing, cloud controls, and defensive engineering.</p><a className="button button-dark" href="#lab-list" onClick={(event) => scrollToId(event, "lab-list")}>Explore projects <ArrowDown aria-hidden="true" /></a></div>
          </Reveal>

          <Reveal><div id="lab-list" className="lab-picker" aria-label="Security learning lab projects">
            <div className="lab-picker-head"><p className="section-kicker">Practice with evidence</p><p>Academic practice, clearly labeled as learning work rather than client engagements.</p></div>
            <div className="lab-card-grid" aria-label="Learning labs">{labs.map((lab) => (
              <button key={lab.id} className={activeLab === lab.id ? "lab-card is-active" : "lab-card"} type="button" aria-pressed={activeLab === lab.id} onClick={() => setActiveLab(lab.id)}>
                <span className="lab-card-number">{lab.number} / LAB</span>
                <h3>{lab.title}</h3>
                <p>{lab.summary}</p>
                <span className="lab-card-evidence"><Check aria-hidden="true" /> {lab.evidence}</span>
                <span className="lab-card-action"><span className="lab-check" aria-hidden="true" /> <span>{activeLab === lab.id ? "Selected" : "Select lab"}</span> <MorphIcon className="morph-icon" icon={activeLab === lab.id ? CheckData : ArrowUpRightData} size={14} strokeWidth={1.5} reducedMotion="user" aria-hidden="true" /></span>
              </button>
            ))}</div>
            <p className="lab-selection" aria-live="polite"><Check aria-hidden="true" /> Selected: {labs.find((lab) => lab.id === activeLab)?.title} <span>·</span> {labs.find((lab) => lab.id === activeLab)?.evidence}</p>
          </div></Reveal>
        </section>

        <section id="experience" className="section experience-section container">
          <Reveal className="experience-heading"><p className="section-kicker">Career log</p><h2>Experience built<br />with intent.</h2><p>Support, teamwork, and security preparation.</p></Reveal>
          <div className="experience-groups">{experienceGroups.map((group) => (
            <Reveal className="experience-group" key={group.label}><p className="group-label">{group.label}</p>{group.entries.map((entry) => (
              <article className="experience-entry" key={entry.role}><p>{entry.period} <span>·</span> {entry.location}</p><h3>{entry.role}</h3><p>{entry.detail}</p></article>
            ))}</Reveal>
          ))}</div>
        </section>
      </main>

      <footer id="contact" className="footer"><div className="container footer-grid">
        <Reveal><p className="section-kicker">Contact</p><h2>Open to thoughtful<br />security work.</h2></Reveal>
        <Reveal className="contact-links"><a href="mailto:chunhao021223@icloud.com"><Mail aria-hidden="true" /> chunhao021223@icloud.com <ArrowUpRight aria-hidden="true" /></a><a href="https://wa.me/60103623937" target="_blank" rel="noreferrer"><Phone aria-hidden="true" /> +60 10-362 3937 <ArrowUpRight aria-hidden="true" /></a><a href="https://github.com/HAO02-CYBER" target="_blank" rel="noreferrer"><GitBranch aria-hidden="true" /> github.com/HAO02-CYBER <ArrowUpRight aria-hidden="true" /></a></Reveal>
      </div></footer>
      </div>
    </>
  );
}

createRoot(document.getElementById("root")).render(<App />);
