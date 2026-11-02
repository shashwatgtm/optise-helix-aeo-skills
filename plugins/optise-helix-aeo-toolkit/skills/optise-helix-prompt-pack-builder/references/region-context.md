# Region and industry reference

Draft for owner review. Use this reference on every invocation before applying sector advice. Read only the matching region, country, vertical and subtype sections below. Data is context for checks, never evidence that a particular company complies or is regulated.

## Selection and output rules

1. Read the user's affirmative selling market. An explicit selling destination wins over headquarters. Ignore competitor locations, customer location without a selling statement, company names, quotes, hypothetical, historical and negated markets. Currency or city clues need unambiguous selling context. Do not infer a market from your own knowledge of a company.
2. If no market is established, keep the sector result and add: Which region applies: India, Southeast Asia, Middle East, UK, Western Europe or North America? Add it to your description and rerun. Do not guess.
3. A broad region never selects a default country. Ask which buyer country applies and use only notes marked COMMON until it is named. For a named country, use only COMMON and its own country code. EU notes apply only to a named EU member country listed here, never the UK, Switzerland or Western Europe as a whole. A US subdivision note requires that state to be named affirmatively.
4. Keep two markets in separate labelled parts, even if both are inside the same region. Do not merge regulations, buying behavior or calculations. A country outside the listed coverage has no sourced note here; say so. Never substitute a nearby country.
5. Match the seller's product to a vertical and, only when established, a subtype in the taxonomy. Do not choose a seller industry from a customer or competitor. Resolve COMMON defaults, the matched vertical and the matched subtype, in that order, keeping all country filters. Remove exact duplicate notes. Do not borrow another subtype's note.
6. Each cell records specific, inherited or waiting_for_source. Inherited adds no distinct note and uses its named parent. Waiting topics are unknown; say that a source is still needed and omit the unverified assertion. If no sourced note matches, say: No sourced note is available for this market and industry combination. No other country has been substituted.
7. Retain every note's applicability condition and source link with checked date when using it. A note is a scoped check, not a conclusion about the buyer. General questions are not facts. Use no unsupported statistic, benchmark, market size, company fact or software recommendation. A software choice goes to https://calendly.com/shashwat-gtmhelix/45min.
8. Apply jurisdiction scope to all other references in this skill too. Older broad sector text must not introduce another country's law or regulator. Keep existing refusals, calculations, evidence limits and output formats. Regional notes do not change arithmetic or prove that generated prose is deterministic. End with an owner action to verify the buyer entity, approval route and missing proof; revisit when the market or data flow changes.

## Index

India: IN. Southeast Asia: read the exact countries in that section. Middle East: read the exact countries in that section. UK: GB. Western Europe: EU membership is listed per country. North America: country and state scopes remain separate.

Data SHA256: 0aced487a60275f9f99305cc012ca3620e287acc8689f71aae39b4fd097a2107

## Taxonomy

logistics-tech = logistics tech
freight-visibility = freight visibility; freight-marketplace = freight marketplaces; seller-shipping = shipping for online sellers; last-mile = last mile delivery; warehousing = warehousing and fulfilment; transport-management = transport and fleet management

fintech = fintech
payments-banking = payments and banking APIs; core-banking = core banking and lending platforms; lending = lending and credit data; wealth-investment = wealth and investment; spend-expense = spend and expense; insurance = insurance

vertical-saas = vertical SaaS
construction = construction management; property-management = property management; field-services = field and home services; fmcg-retail-execution = FMCG retail execution; industry-hr-payroll = HR and payroll built for one industry; hotel-lodging = hotels and lodging operations; retail-restaurant-ops = retail, restaurant and distribution operations

ai-native = AI native
agents-copilots = AI agents and copilots for a business function; voice-language-models = voice and language models; enterprise-search = enterprise search and work assistants; document-ai = document AI and intelligent document processing; ai-video = AI video for training and communications

ites = ITeS
it-services = IT services and application services; bpo-cx = BPO and customer experience outsourcing; digital-engineering = digital engineering and product engineering; data-services = data and analytics services; engineering-talent = engineering talent and team augmentation

telecom = telecom
operators-connectivity = operators and enterprise connectivity; cpaas-messaging = CPaaS and messaging; telecom-software = software and clearing services sold to operators; business-voice-ucaas = business voice and unified communications; iot-connectivity = IoT connectivity

cybersecurity = cybersecurity
cloud-security = cloud security; identity-security = identity and access; email-security = email security; awareness-training = security awareness and human risk; appsec = application and developer security; mobile-appsec = mobile application security; soc-services = managed detection and SOC services; endpoint-network = endpoint and network security; pentest = penetration testing and offensive security; attack-surface-dast = external attack surface and dynamic testing

software = software
developer-platform = developer platforms and DevOps; data-infrastructure = managed data infrastructure; observability = observability and application monitoring; testing = testing and QA tools; dev-tools = containers and developer environments; process-orchestration = process orchestration and workflow engines; open-source-support = open source software support and services

saas = SaaS
customer-service = customer service software; crm-marketing = CRM and marketing; collaboration = collaboration and work management; product-growth = product analytics and customer success; product-management = product management software; digital-adoption = digital adoption platforms

## India

Draft for owner review. India only. Each rule is conditional on entity, activity and commencement. IFSC financial activities require their own scope check. Questions are discovery prompts, not claims about all Indian buyers. No payment term, language preference or purchasing habit is assumed.
Countries: IN = India
Clues, only in selling context: {"aliases":["India"],"countries":[{"code":"IN","name":"India","aliases":["India","Bharat"],"cities":["Bengaluru","Bangalore","Mumbai","New Delhi","Chennai","Hyderabad","Pune"],"currencies":["INR","Indian rupee"],"regulators":["Reserve Bank of India","RBI","Securities and Exchange Board of India","SEBI","Insurance Regulatory and Development Authority of India","IRDAI","Telecom Regulatory Authority of India","TRAI"]}]}

### Defaults

decision_approvers | scope IN | question: Who owns the budget, security review, data permissions and final purchase approval for this Indian buyer?

procurement_payment | scope IN | question: What purchase order, invoice acceptance, currency and payment terms has this buyer actually agreed?

data_privacy | scope IN | legal: India: the Digital Personal Data Protection Rules, 2025 have staged commencement. Have the privacy owner map each proposed obligation to its effective date before promising compliance.
Applies only: For processing in scope of the Digital Personal Data Protection Act, 2023. Do not treat later commencing rules as already effective.
Source I:IN-DPDP: Digital Personal Data Protection Rules, 2025 <https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf>. Checked 2026-11-03. Gazette dated 13 November; ministry listing published 14 November 2025. Most operational rules have later commencement. Do not describe the full regime as already operative.

buyer_language | scope IN | question: Which languages must the Indian buying team and end users understand in the proposal, notices and support?

proof | scope IN | question: Which workflow, sample data and acceptance evidence will the buyer approve before a wider rollout?

objections | scope IN | question: Which unresolved data access, integration, support or contract issue could prevent this purchase?

sales_motion | scope IN | question: Who will own a limited evaluation, its acceptance decision and the next purchase step?

### logistics-tech | specific | inherits defaults
Inherit applicable parent notes, then add only the sourced country and activity specific notes below.

sector_regulator | scope IN | legal: India: Rule 138 of the Central Goods and Services Tax Rules, 2017 links qualifying goods movements to an e way bill workflow. Establish whether the consignor, consignee or transporter owns the record.
Applies only: Only for goods movements within the rule, subject to exemptions and current central and state requirements. Selling logistics software does not itself make the vendor the transporter.
Source I:IN-EWB: E Way Bill System FAQs <https://docs.ewaybillgst.gov.in/html/faq.html>. Checked 2026-11-03. No reliable publication date. Some portal instructions are visibly old. Used only for workflow ownership; no thresholds, validity distance or current API rules asserted.

proof | scope IN | question: Can the operator demonstrate the handoff from shipment documents to the transport record, including corrections and responsibility for exceptions?

### fintech | specific | inherits defaults
Inherit applicable parent notes, then add only the sourced country and activity specific notes below.

decision_approvers | scope IN | legal: For a commercial bank in scope, the 2025 outsourcing directions retain responsibility with its board and senior management and require an approved outsourcing policy.
Applies only: For the banks and outsourcing arrangements covered by the Reserve Bank of India (Commercial Banks: Managing Risks in Outsourcing) Directions, 2025.
Source I:IN-RBI-OUTSOURCE: Reserve Bank of India (Commercial Banks: Managing Risks in Outsourcing) Directions, 2025 <https://pdicai.org/Docs/RBI-DOR-2025-26-171_512202515451570.pdf>. Checked 2026-11-03. Original RBI instrument hosted by ICAI. Direct RBI URL could not be retrieved. This text excludes several bank categories. Check amendments before release.

sector_regulator | scope IN | legal: India: identify the financial activity and the buyer's regulated entity category before selecting an RBI outsourcing instrument.
Applies only: This source covers specified commercial banks. It excludes small finance banks, local area banks, payments banks and regional rural banks; do not apply it to those entities or NBFCs.
Source I:IN-RBI-OUTSOURCE: Reserve Bank of India (Commercial Banks: Managing Risks in Outsourcing) Directions, 2025 <https://pdicai.org/Docs/RBI-DOR-2025-26-171_512202515451570.pdf>. Checked 2026-11-03. Original RBI instrument hosted by ICAI. Direct RBI URL could not be retrieved. This text excludes several bank categories. Check amendments before release.

proof | scope IN | question: Ask the bank to confirm whether the proposed IT service is material outsourcing and which risk review and approval evidence it requires.
Applies only: For the proposed bank service only.

### vertical-saas | inherited | inherits defaults
Reviewed: no validated sector override beyond the country defaults. This is not a finding that no sector law applies.

### ai-native | specific | inherits defaults
Inherit applicable parent notes, then add only the sourced country and activity specific notes below.

proof | scope IN | operating: India's AI Governance Guidelines recommend accountable and understandable systems. Use an evaluation showing failure handling, human responsibility and risks in the intended Indian use case.
Applies only: Government guidance for AI development or deployment in India. These recommendations do not establish mandatory certification.
Source I:IN-AI: India AI Governance Guidelines <https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2228315&lang=2&reg=48>. Checked 2026-11-03. Policy guidance is not a blanket certification or new licence. Binding sector laws remain separate.

### ites | specific | inherits defaults
Inherit applicable parent notes, then add only the sourced country and activity specific notes below.

sector_regulator | scope IN | legal: India: DoT's Revised Guidelines for Other Service Providers address the defined OSP activity. Check whether the service is voice based BPO before applying that framework.
Applies only: Only a service within the OSP definition; not every IT outsourcing engagement.
Source I:IN-OSP: Revised Guidelines for Other Service Providers <https://www.dot.gov.in/static/uploads/2025/08/4e6e21029dc45f42b4e1e57e6300fa72.pdf>. Checked 2026-11-03. Do not treat every IT service or software vendor as an OSP. Verify later changes for the actual service.

### telecom | specific | inherits defaults
Inherit applicable parent notes, then add only the sourced country and activity specific notes below.

sector_regulator | scope IN | legal: India: DoT opened the authorisation and licence migration route under the Telecommunications Act, 2023 in June 2026. Confirm the service category and current authorisation with the operator.
Applies only: For providing a telecommunications service or migrating an existing licence; do not assume operator authorisation applies to a software supplier.
Source I:IN-DOT: Telecommunication service authorisations and licence migration <https://www.pib.gov.in/PressReleasePage.aspx?PRID=2277786&lang=1&reg=3>. Checked 2026-11-03. Announcement supports the authorisation route only. Service specific eligibility must be checked in current rules.

### cybersecurity | specific | inherits defaults
Inherit applicable parent notes, then add only the sourced country and activity specific notes below.

sector_regulator | scope IN | legal: India: CERT In's directions under section 70B of the Information Technology Act, 2000 include incident reporting and contact requirements. Agree who classifies and reports applicable incidents.
Applies only: For entities and incidents within the directions and accompanying FAQs. An alert alone is not evidence of a reportable breach.
Source I:IN-CERT: Frequently Asked Questions on Cyber Security Directions of 28 April 2022 <https://www.cert-in.org.in/PDF/FAQs_on_CyberSecurityDirections_May2022.pdf>. Checked 2026-11-03. FAQ publication date confirmed by PIB release of 18 May 2022. Read with directions; do not infer that every incident or every security product is within each provision.

proof | scope IN | operating: Ask for a demonstration of relevant event logs, reliable timestamps and the escalation path that supports the customer's CERT In duties.
Applies only: Only where the customer and service fall within the directions; this is suggested evidence, not a compliance certificate.
Source I:IN-CERT: Frequently Asked Questions on Cyber Security Directions of 28 April 2022 <https://www.cert-in.org.in/PDF/FAQs_on_CyberSecurityDirections_May2022.pdf>. Checked 2026-11-03. FAQ publication date confirmed by PIB release of 18 May 2022. Read with directions; do not infer that every incident or every security product is within each provision.

### software | inherited | inherits defaults
Reviewed: no validated sector override beyond the country defaults. This is not a finding that no sector law applies.

### saas | inherited | inherits defaults
Reviewed: no validated sector override beyond the country defaults. This is not a finding that no sector law applies.

### freight-visibility | inherited | inherits logistics-tech
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### freight-marketplace | inherited | inherits logistics-tech
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### seller-shipping | inherited | inherits logistics-tech
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### last-mile | inherited | inherits logistics-tech
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### warehousing | inherited | inherits logistics-tech
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### transport-management | inherited | inherits logistics-tech
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### payments-banking | specific | inherits fintech
Inherit applicable parent notes, then add only the sourced country and activity specific notes below.

sector_regulator | scope IN | legal: India: the Payment and Settlement Systems Act, 2007 places payment system authorisation with RBI, subject to statutory exceptions. Separate the system operator from its software supplier.
Applies only: For operating a payment system in the Act's scope. IFSC activities require the separate statutory boundary check.
Source I:IN-PSS: Payment and Settlement Systems Act, 2007 <https://financialservices.gov.in/sites/default/files/Act-Policies/2026-01/Payment-and-Settlement-Systems-Act_2007.pdf>. Checked 2026-11-03. Check statutory exceptions and IFSC scope. Does not establish that selling payment software is operating a payment system.

### core-banking | inherited | inherits fintech
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### lending | waiting_for_source | inherits fintech
Keep the parent notes only within their scope. Do not extend commercial bank directions to every lender.
Waiting for a source: Verify the current entity specific digital lending instrument on a primary source before adding digital lending obligations.

### wealth-investment | specific | inherits fintech
Inherit applicable parent notes, then add only the sourced country and activity specific notes below.

sector_regulator | scope IN | legal: India: SEBI lists distinct regulations for investment advisers, research analysts, brokers, funds and portfolio managers. Identify the actual service before choosing the applicable instrument.
Applies only: For securities activity within SEBI scope. A software vendor is not automatically a licensed financial intermediary.
Source I:IN-SEBI: Updated list of SEBI regulations <https://sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=2&smid=0&ssid=3>. Checked 2026-11-03. Live index has no single publication date. Identifies instruments only; does not validate licensing requirements or every underlying rule.

### spend-expense | inherited | inherits fintech
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### insurance | specific | inherits fintech
Inherit applicable parent notes, then add only the sourced country and activity specific notes below.

sector_regulator | scope IN | legal: India: the Insurance Regulatory and Development Authority Act, 1999 assigns insurance supervision to IRDAI. Identify the insurer or intermediary role before mapping obligations.
Applies only: For insurance activities in scope; check the IFSC exclusion and the current product specific instrument.
Source I:IN-IRDAI: Insurance Regulatory and Development Authority Act, 1999 <https://www.indiacode.nic.in/bitstream/123456789/1893/1/A1999_41.pdf>. Checked 2026-11-03. Used only for regulator boundary. Product specific current regulations require separate checks.

### customer-service | inherited | inherits saas
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### crm-marketing | inherited | inherits saas
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### collaboration | inherited | inherits saas
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### product-growth | inherited | inherits saas
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### construction | inherited | inherits vertical-saas
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### property-management | inherited | inherits vertical-saas
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### field-services | inherited | inherits vertical-saas
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### fmcg-retail-execution | inherited | inherits vertical-saas
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### industry-hr-payroll | inherited | inherits vertical-saas
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### hotel-lodging | inherited | inherits vertical-saas
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### retail-restaurant-ops | inherited | inherits vertical-saas
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### agents-copilots | inherited | inherits ai-native
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### voice-language-models | inherited | inherits ai-native
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### enterprise-search | inherited | inherits ai-native
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### it-services | inherited | inherits ites
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### bpo-cx | inherited | inherits ites
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### digital-engineering | inherited | inherits ites
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### data-services | inherited | inherits ites
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### operators-connectivity | inherited | inherits telecom
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### cpaas-messaging | specific | inherits telecom
Inherit applicable parent notes, then add only the sourced country and activity specific notes below.

sector_regulator | scope IN | legal: India: TRAI's Telecom Commercial Communications Customer Preference Regulations, 2018 address registered senders and customer preference and consent. Map the intended commercial messaging route before launch.
Applies only: For commercial communications within the telecom framework; verify the current consolidated rules and amendments.
Source I:IN-TRAI: TRAI strengthens consumer protection with amendments to TCCCPR, 2018 <https://www.pib.gov.in/PressReleasePage.aspx?PRID=2102413&lang=2&reg=48>. Checked 2026-11-03. Announcement rather than consolidated regulations. No detailed number series or timing requirement asserted.

### telecom-software | inherited | inherits telecom
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### business-voice-ucaas | inherited | inherits telecom
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### developer-platform | inherited | inherits software
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### data-infrastructure | inherited | inherits software
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### observability | inherited | inherits software
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### testing | inherited | inherits software
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### dev-tools | inherited | inherits software
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### cloud-security | inherited | inherits cybersecurity
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### identity-security | inherited | inherits cybersecurity
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### email-security | inherited | inherits cybersecurity
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### awareness-training | inherited | inherits cybersecurity
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### appsec | inherited | inherits cybersecurity
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### mobile-appsec | inherited | inherits cybersecurity
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### soc-services | inherited | inherits cybersecurity
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### endpoint-network | inherited | inherits cybersecurity
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### document-ai | inherited | inherits ai-native
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### ai-video | inherited | inherits ai-native
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### engineering-talent | inherited | inherits ites
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### product-management | inherited | inherits saas
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### digital-adoption | inherited | inherits saas
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### pentest | inherited | inherits cybersecurity
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### attack-surface-dast | inherited | inherits cybersecurity
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### process-orchestration | inherited | inherits software
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### open-source-support | inherited | inherits software
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

### iot-connectivity | inherited | inherits telecom
Reviewed: no validated country difference beyond the parent cell for this subtype. Inherit the parent; this is not a finding that no additional law applies.

## Southeast Asia

Draft for owner review. Country notes currently cover Singapore, Indonesia, Malaysia, Thailand, Viet Nam and the Philippines to the extent sourced below. They do not establish complete legal coverage. Brunei, Cambodia, Laos, Myanmar and Timor Leste are recognised but await country sources. A broad regional request needs a country before country law can be selected. Questions do not assert local buying habits.
Countries: SG = Singapore; ID = Indonesia; MY = Malaysia; TH = Thailand; VN = Viet Nam; PH = Philippines; BN = Brunei; KH = Cambodia; LA = Laos; MM = Myanmar; TL = Timor Leste
Clues, only in selling context: {"aliases":["Southeast Asia","South East Asia"],"countries":[{"code":"SG","name":"Singapore","aliases":[],"cities":[],"currencies":["SGD","Singapore dollar"],"regulators":["Monetary Authority of Singapore"]},{"code":"ID","name":"Indonesia","aliases":[],"cities":["Jakarta","Surabaya"],"currencies":["IDR","Indonesian rupiah"],"regulators":["Bank Indonesia","Otoritas Jasa Keuangan"]},{"code":"MY","name":"Malaysia","aliases":[],"cities":["Kuala Lumpur"],"currencies":["MYR","Malaysian ringgit"],"regulators":["Bank Negara Malaysia"]},{"code":"TH","name":"Thailand","aliases":[],"cities":["Bangkok"],"currencies":["THB","Thai baht"],"regulators":["Bank of Thailand"]},{"code":"VN","name":"Viet Nam","aliases":["Vietnam"],"cities":["Hanoi","Ho Chi Minh City"],"currencies":["VND","Vietnamese dong"],"regulators":[]},{"code":"PH","name":"Philippines","aliases":["the Philippines"],"cities":["Manila","Cebu"],"currencies":["PHP","Philippine peso"],"regulators":["Bangko Sentral ng Pilipinas"]},{"code":"BN","name":"Brunei","aliases":["Brunei Darussalam"],"cities":["Bandar Seri Begawan"],"currencies":["BND"],"regulators":[]},{"code":"KH","name":"Cambodia","aliases":[],"cities":["Phnom Penh"],"currencies":["KHR"],"regulators":[]},{"code":"LA","name":"Laos","aliases":["Lao PDR"],"cities":["Vientiane"],"currencies":["LAK"],"regulators":[]},{"code":"MM","name":"Myanmar","aliases":[],"cities":["Yangon","Naypyidaw"],"currencies":["MMK"],"regulators":[]},{"code":"TL","name":"Timor Leste","aliases":["Timor-Leste","East Timor"],"cities":["Dili"],"currencies":[],"regulators":[]}]}

### Defaults

decision_approvers | scope COMMON | question: Which named country and contracting entity are in scope, and who approves budget, risk and the purchase?

procurement_payment | scope COMMON | question: What currency, purchase order, invoice acceptance and payment terms has this buyer confirmed?

data_privacy | scope SG | legal: Singapore: the Personal Data Protection Act requires appropriate protection and retention controls and comparable protection for overseas transfers. Map where personal data goes and who controls it.
Applies only: For organisations and processing in the Act's scope, subject to applicable exclusions and transfer regulations.
Source I:SG-PDPA: Data protection obligations under the Personal Data Protection Act <https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Resource-for-Organisation/Data-Protection-Obligations-under-the-PDPA.ashx?la=en>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Document states May 2021. Used only for these stable obligations, not its uncommenced data portability item. Check exceptions and current regulations.

data_privacy | scope ID | legal: Indonesia: check the proposed processing against Law No. 27 of 2022 on Personal Data Protection before agreeing data access and transfer terms.
Applies only: For processing within the Indonesian law's scope. Detailed implementing requirements must be checked for the actual data flow.
Source I:ID-PDP: Law No. 27 of 2022 on Personal Data Protection <https://jdih.komdigi.go.id/produk_hukum/view/id/832/t/crc32/>. Checked 2026-11-03. Primary indexed law entry read; live open timed out. Detailed transfer mechanisms and implementing rules not asserted.

data_privacy | scope MY | legal: Malaysia: the Personal Data Protection Act 2010 applies to personal data in commercial transactions within its scope; federal and state governments are excluded.
Applies only: Check establishment, processing location and statutory exclusions. Read the Act with its amendments.
Source I:MY-PDPA: Application and non application of the Personal Data Protection Act <https://www.pdp.gov.my/en/akta/application-and-non-application-of-the-act/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Used only for scope. Read Act 709 as amended and current commencement instruments before specific obligations.

data_privacy | scope PH | legal: Philippines: Republic Act 10173, the Data Privacy Act of 2012, sets lawful processing and security requirements. Identify the personal information controller and processor roles.
Applies only: For processing in the Act's scope, with separate treatment for sensitive personal information and statutory exceptions.
Source I:PH-DPA: Republic Act 10173: Data Privacy Act of 2012 <https://privacy.gov.ph/data-privacy-act/>. Checked 2026-11-03. Statutory exclusions, sensitive information rules and current implementing instruments require scope review.

data_privacy | scope TH | legal: Thailand: use the Personal Data Protection Act B.E. 2562 (2019) for the local privacy scope review. Confirm the controller, processor and proposed data use.
Applies only: For Thai processing in scope; this note does not determine the lawful basis or transfer mechanism.
Source I:TH-PDPA: Personal Data Protection Act B.E. 2562 (2019) <https://mdes.go.th/law/128>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Index identifies law; no specific consent, transfer or reporting deadline asserted.

data_privacy | scope VN | legal: Viet Nam: the Law on Personal Data Protection took effect on 1 January 2026. Review the current law and implementing rules before finalising data handling terms.
Applies only: For processing in scope of the Vietnamese regime. An older decree alone is not a complete current review.
Source I:VN-PDP: Presidential Office announces new laws <https://en.baochinhphu.vn/presidential-office-announces-18-new-laws-111250711204559004.htm>. Checked 2026-11-03. Announcement used for commencement only. No penalties or detailed transfer rules reproduced.

buyer_language | scope COMMON | question: Which languages do the buying team, users and required notices need?

proof | scope COMMON | question: What sample workflow and acceptance evidence will the buyer approve?

objections | scope COMMON | question: Which data access, integration, support or contract issue could block the purchase?

sales_motion | scope COMMON | question: Who owns the evaluation, acceptance decision and next purchase step?

### logistics-tech | waiting_for_source | inherits defaults
Inherit only applicable parent notes, then add these country and activity specific differences.
Waiting for a source: Complete sector source checks for countries without an applicable note; never substitute a neighbouring country's rule.

sector_regulator | scope SG | legal: Singapore: import permits use the Singapore Customs TradeNet process. Confirm whether the importer submits the declaration or appoints a declaring agent.
Applies only: For goods imported into Singapore within the applicable permit requirements. A logistics software vendor is not automatically the declaring agent.
Source I:SG-CUSTOMS: Obtain a Customs Import Permit <https://www.customs.gov.sg/doing-business/import-operations/import-procedures/obtain-a-customs-import-permit/>. Checked 2026-11-03. Page update date. Exceptions and controlled goods requirements remain activity specific.

### fintech | waiting_for_source | inherits defaults
Inherit only applicable parent notes, then add these country and activity specific differences.
Waiting for a source: Complete sector source checks for countries without an applicable note; never substitute a neighbouring country's rule.

decision_approvers | scope SG | question: Ask the institution which outsourcing governance and risk approval process applies, and which evidence the supplier must provide.
Applies only: For the proposed Singapore financial institution engagement.

sector_regulator | scope SG | legal: Singapore: MAS distinguishes bank outsourcing notices and guidance from guidance for other financial institutions. Classify the buyer before choosing the review.
Applies only: For a financial institution and outsourcing arrangement within the relevant MAS instrument; a consultation is not a final rule.
Source I:SG-OUTSOURCE: Third party risk management <https://www.mas.gov.sg/regulation/third-party-risk-management>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Index last updated 6 March 2026. Distinguish a notice from guidelines and from a consultation; no universal vendor licence inferred.

sector_regulator | scope ID | legal: Indonesia: OJK supervises banking, insurance, financing and capital market activities within its remit. Select the activity before requesting its compliance evidence.
Applies only: For an OJK supervised entity or activity. Payment system matters require the separately scoped payment note.
Source I:ID-OJK: Task and Functions <https://ojk.go.id/en/tentang-ojk/Pages/Tugas-dan-Fungsi.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Do not infer that OJK replaces Bank Indonesia's payment remit.

sector_regulator | scope MY | legal: Malaysia: Bank Negara Malaysia supervises banking and insurance and takaful institutions under its remit. Confirm the buyer's category.
Applies only: For institutions within BNM supervision; do not extend this to all lenders or securities activities.
Source I:MY-BNM: Supervision <https://www.bnm.gov.my/supervision>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Does not cover every nonbank lender or every capital market service.

sector_regulator | scope PH | legal: Philippines: BSP supervises banks and other institutions within its remit and oversees payment systems. Confirm whether the actual buyer is BSP supervised.
Applies only: Only for BSP supervised entities and activities.
Source I:PH-BSP: Governance of the Bank <https://www.bsp.gov.ph/Pages/AboutTheBank/WhoWeAre/OrganizationAndGovernance/GovernanceOfTheBank.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Not all lenders or insurers are BSP regulated.

sector_regulator | scope TH | legal: Thailand: the Bank of Thailand supervises financial institutions and has payment system responsibilities. Confirm the institution and product before selecting requirements.
Applies only: Only for the Bank of Thailand's actual supervisory scope.
Source I:TH-BOT: Our Roles <https://www.bot.or.th/en/our-roles.html>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Does not establish oversight of every finance or insurance business.

### vertical-saas | inherited | inherits defaults
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### ai-native | specific | inherits defaults
Inherit only applicable parent notes, then add these country and activity specific differences.

proof | scope SG | operating: Singapore's Model AI Governance Framework for Agentic AI recommends human accountability and controls on agent actions. Show approval boundaries and failure handling in the evaluation.
Applies only: Guidance for agentic AI deployment, not a certification or general software licence.
Source I:SG-AI: Updated Model AI Governance Framework for Agentic AI <https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/factsheets/2026/updated-model-ai-governance-framework-for-agentic-ai>. Checked 2026-11-03. Primary indexed extract read; live open returned a script challenge. Guidance, not a mandatory certification.

### ites | inherited | inherits defaults
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### telecom | waiting_for_source | inherits defaults
Inherit only applicable parent notes, then add these country and activity specific differences.
Waiting for a source: Complete sector source checks for countries without an applicable note; never substitute a neighbouring country's rule.

sector_regulator | scope SG | legal: Singapore: IMDA's Services Based Operations licence covers defined telecommunications service operations. Confirm whether the seller operates a service or supplies software to an operator.
Applies only: Only for the activity within the relevant Singapore licensing category.
Source I:SG-TELECOM: Services Based Operations licence <https://www.imda.gov.sg/regulations-and-licensing-listing/services-based-operations--sbo--licence>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Primary indexed page extract read; live open returned a script challenge. No specific licence conditions asserted.

### cybersecurity | waiting_for_source | inherits defaults
Inherit only applicable parent notes, then add these country and activity specific differences.
Waiting for a source: Complete sector source checks for countries without an applicable note; never substitute a neighbouring country's rule.

sector_regulator | scope SG | legal: Singapore: the Cybersecurity Act licensing framework covers penetration testing and managed security operations centre monitoring services. Check the exact service scope.
Applies only: For licensable services under the Act. Do not classify every cybersecurity product as a licensed service.
Source I:SG-CYBER: Cybersecurity Act <https://www.csa.gov.sg/legislation/cybersecurity-act/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Live page used for service scope only. Other cybersecurity obligations and amended designation regimes require separate applicability review.

### software | inherited | inherits defaults
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### saas | inherited | inherits defaults
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### freight-visibility | inherited | inherits logistics-tech
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### freight-marketplace | inherited | inherits logistics-tech
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### seller-shipping | inherited | inherits logistics-tech
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### last-mile | inherited | inherits logistics-tech
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### warehousing | inherited | inherits logistics-tech
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### transport-management | inherited | inherits logistics-tech
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### payments-banking | waiting_for_source | inherits fintech
Inherit only applicable parent notes, then add these country and activity specific differences.
Waiting for a source: Complete this activity's country coverage beyond the explicitly sourced notes.

sector_regulator | scope SG | legal: Singapore: the Payment Services Act 2019 regulates defined payment services and exemptions. Map the actual money flow and service before choosing the MAS licence category.
Applies only: For a payment service within the Act, not every supplier of payment software.
Source I:SG-PAYMENTS: Payments regulation <https://www.mas.gov.sg/regulation/payments>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Does not establish that all payment software suppliers provide a regulated service.

sector_regulator | scope ID | legal: Indonesia: Bank Indonesia's PBI 10 of 2025 and PADG 32 of 2025 govern the payment system industry from 31 March 2026. Map the provider and supporting party roles.
Applies only: For the payment activity and entities in scope; no licence or exemption is inferred.
Source I:ID-PAYMENTS: Bank Indonesia strengthens structure of payment system industry <https://www.bi.go.id/en/publikasi/ruang-media/news-release/Pages/sp_281626.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Announcement used to identify the current framework and third party risk focus. No financial projection or statistic used.

### core-banking | inherited | inherits fintech
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### lending | waiting_for_source | inherits fintech
Inherit only applicable parent notes, then add these country and activity specific differences.
Waiting for a source: Complete this activity's country coverage beyond the explicitly sourced notes.

sector_regulator | scope SG | legal: Singapore: licensed moneylenders fall under the Ministry of Law Registry of Moneylenders. Its rules include physical identity verification and do not allow a fully online loan transaction.
Applies only: Only licensed moneylenders under that regime; do not apply this condition to bank lending.
Source I:SG-LENDING: List of licensed moneylenders in Singapore <https://rom.mlaw.gov.sg/information-for-borrowers/list-of-licensed-moneylenders-in-singapore/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. This rule is for licensed moneylenders, not every bank or financial institution. No entity names copied.

sector_regulator | scope ID | legal: Indonesia: POJK 40 of 2024 addresses technology based joint funding services. Establish whether the platform is an intermediary in that regime before mapping OJK requirements.
Applies only: For LPBBTI activity only, not all lending or credit data software.
Source I:ID-LENDING: POJK 40 Tahun 2024 Layanan Pendanaan Bersama Berbasis Teknologi Informasi <https://ojk.go.id/id/regulasi/Pages/POJK-40-Tahun-2024-Layanan-Pendanaan-Bersama-Berbasis-Teknologi-Informasi.aspx>. Checked 2026-11-03. Entry gives effective date. Primary indexed abstract read; live open timed out. Do not extend P2P rules to every lender.

sector_regulator | scope PH | legal: Philippines: lending companies under the Lending Company Regulation Act, RA 9474, need the SEC authority for that business. Distinguish this entity from a BSP supervised bank.
Applies only: Only companies within RA 9474; software supply alone does not establish that activity.
Source I:PH-LENDING: Frequently asked questions on lending companies <https://www.sec.gov.ph/wp-content/uploads/2019/11/2019FAQ_LendingCompanies.pdf>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Undated FAQ. Used only for basic entity boundary; no capital requirement or current platform procedure asserted.

### wealth-investment | waiting_for_source | inherits fintech
Inherit only applicable parent notes, then add these country and activity specific differences.
Waiting for a source: Complete this activity's country coverage beyond the explicitly sourced notes.

sector_regulator | scope SG | legal: Singapore: regulated financial advice under the Financial Advisers Act 2001 requires the relevant MAS licence unless exempt. Separate advice from general information or software supply.
Applies only: For the actual regulated activity and applicable exemptions.
Source I:SG-ADVISERS: Financial adviser's licence <https://www.mas.gov.sg/regulation/capital-markets/apply-for-licensing-or-registration-of-capital-market-entities/financial-advisers>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Investment advice is distinct from general financial software.

sector_regulator | scope ID | legal: Indonesia: OJK supervises capital market activities in its remit. Identify the investment service and regulated entity.
Applies only: For capital market activities in Indonesia within OJK's authority.
Source I:ID-OJK: Task and Functions <https://ojk.go.id/en/tentang-ojk/Pages/Tugas-dan-Fungsi.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Do not infer that OJK replaces Bank Indonesia's payment remit.

sector_regulator | scope MY | legal: Malaysia: Securities Commission Malaysia regulates capital market services under the Capital Markets and Services Act 2007. Map the actual regulated activity.
Applies only: For capital market entities and services within that Act.
Source I:MY-SC: About the Securities Commission Malaysia <https://www.sc.com.my/about/about/about-the-sc>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Entity and activity licensing must be checked separately.

sector_regulator | scope TH | legal: Thailand: the Securities and Exchange Commission supervises the Thai capital market. Establish the investment activity and regulated entity before selecting obligations.
Applies only: For capital market activities within the Thai SEC's remit.
Source I:TH-SEC: Enforcement <https://www.sec.or.th/EN/pages/lawandregulations/enforcement.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Not every wealth related software activity needs the same authorisation.

### spend-expense | inherited | inherits fintech
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### insurance | waiting_for_source | inherits fintech
Inherit only applicable parent notes, then add these country and activity specific differences.
Waiting for a source: Complete this activity's country coverage beyond the explicitly sourced notes.

sector_regulator | scope SG | legal: Singapore: MAS is the responsible agency for the Insurance Act 1966. Identify whether the buyer is an insurer, insurance intermediary or another service provider.
Applies only: For insurance business and entities within the Act; no licence conclusion for a software vendor.
Source I:SG-INSURANCE: Sectoral legislation with ownership and control provisions <https://www.osir.gov.sg/resources/other-legislation/sectoral-legislation/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Used to identify regulator and legal instrument, not detailed ownership approval conditions.

sector_regulator | scope ID | legal: Indonesia: OJK's remit includes insurance. Have the insurer or intermediary identify the current instrument for its activity.
Applies only: For insurance entities under OJK supervision.
Source I:ID-OJK: Task and Functions <https://ojk.go.id/en/tentang-ojk/Pages/Tugas-dan-Fungsi.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Do not infer that OJK replaces Bank Indonesia's payment remit.

sector_regulator | scope MY | legal: Malaysia: Bank Negara Malaysia's insurance and takaful supervision covers the institutions within its remit. Confirm the insurance or takaful entity before the compliance review.
Applies only: For the applicable BNM supervised institution.
Source I:MY-BNM: Supervision <https://www.bnm.gov.my/supervision>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Does not cover every nonbank lender or every capital market service.

sector_regulator | scope PH | legal: Philippines: the Insurance Commission supervises insurance under the Insurance Code. Start the review with the insurer or intermediary's actual role.
Applies only: For insurance activity within the Commission's remit.
Source I:PH-INSURANCE: Mandate, objectives and functions <https://site.insurance.gov.ph/about/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Not a licence determination for a software provider.

### customer-service | inherited | inherits saas
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### crm-marketing | inherited | inherits saas
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### collaboration | inherited | inherits saas
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### product-growth | inherited | inherits saas
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### construction | inherited | inherits vertical-saas
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### property-management | inherited | inherits vertical-saas
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### field-services | inherited | inherits vertical-saas
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### fmcg-retail-execution | inherited | inherits vertical-saas
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### industry-hr-payroll | inherited | inherits vertical-saas
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### hotel-lodging | inherited | inherits vertical-saas
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### retail-restaurant-ops | inherited | inherits vertical-saas
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### agents-copilots | inherited | inherits ai-native
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### voice-language-models | inherited | inherits ai-native
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### enterprise-search | inherited | inherits ai-native
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### it-services | inherited | inherits ites
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### bpo-cx | inherited | inherits ites
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### digital-engineering | inherited | inherits ites
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### data-services | inherited | inherits ites
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### operators-connectivity | inherited | inherits telecom
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### cpaas-messaging | inherited | inherits telecom
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### telecom-software | inherited | inherits telecom
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### business-voice-ucaas | inherited | inherits telecom
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### developer-platform | inherited | inherits software
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### data-infrastructure | inherited | inherits software
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### observability | inherited | inherits software
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### testing | inherited | inherits software
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### dev-tools | inherited | inherits software
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### cloud-security | inherited | inherits cybersecurity
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### identity-security | inherited | inherits cybersecurity
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### email-security | inherited | inherits cybersecurity
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### awareness-training | inherited | inherits cybersecurity
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### appsec | inherited | inherits cybersecurity
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### mobile-appsec | inherited | inherits cybersecurity
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### soc-services | inherited | inherits cybersecurity
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### endpoint-network | inherited | inherits cybersecurity
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### document-ai | inherited | inherits ai-native
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### ai-video | inherited | inherits ai-native
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### engineering-talent | inherited | inherits ites
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### product-management | inherited | inherits saas
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### digital-adoption | inherited | inherits saas
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### pentest | inherited | inherits cybersecurity
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### attack-surface-dast | inherited | inherits cybersecurity
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### process-orchestration | inherited | inherits software
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### open-source-support | inherited | inherits software
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

### iot-connectivity | inherited | inherits telecom
No validated additional subtype or sector override was established in the sourced countries. Inherit only notes for the named country. Unsourced countries remain outside factual coverage.

## Middle East

Draft for owner review. Sourced notes currently cover the UAE and Saudi Arabia only. Qatar, Bahrain, Oman and Kuwait are recognised but awaiting local sources. No Gulf wide regulatory or buying habit claim is made. UAE federal, DIFC and ADGM scopes must be distinguished; a city alone does not select a financial free zone. Other Middle East jurisdictions are not covered by this draft and must never inherit either country's law.
Countries: AE = United Arab Emirates; SA = Saudi Arabia; QA = Qatar; BH = Bahrain; OM = Oman; KW = Kuwait
Clues, only in selling context: {"aliases":["Middle East","Gulf","GCC"],"countries":[{"code":"AE","name":"United Arab Emirates","aliases":["UAE"],"cities":["Dubai","Abu Dhabi","Sharjah"],"currencies":["AED","UAE dirham"],"regulators":["Central Bank of the United Arab Emirates","CBUAE","Dubai Financial Services Authority","DFSA","Financial Services Regulatory Authority","FSRA","Telecommunications and Digital Government Regulatory Authority","TDRA"]},{"code":"SA","name":"Saudi Arabia","aliases":["Kingdom of Saudi Arabia","KSA"],"cities":["Riyadh","Jeddah","Dammam"],"currencies":["SAR","Saudi riyal"],"regulators":["Saudi Central Bank","SAMA","Saudi Data and AI Authority","SDAIA","Zakat Tax and Customs Authority","ZATCA"]},{"code":"QA","name":"Qatar","aliases":[],"cities":["Doha"],"currencies":["QAR","Qatari riyal"],"regulators":[]},{"code":"BH","name":"Bahrain","aliases":[],"cities":["Manama"],"currencies":["BHD","Bahraini dinar"],"regulators":[]},{"code":"OM","name":"Oman","aliases":[],"cities":["Muscat"],"currencies":["OMR","Omani rial"],"regulators":[]},{"code":"KW","name":"Kuwait","aliases":[],"cities":["Kuwait City"],"currencies":["KWD","Kuwaiti dinar"],"regulators":[]}]}

### Defaults

decision_approvers | scope COMMON | question: Which country, legal entity and activity are in scope, and who approves budget, risk and the purchase?

procurement_payment | scope AE | legal: UAE: electronic invoicing is being implemented in phases. Have the finance owner establish the entity's applicable implementation and preparation dates from the current FTA notice.
Applies only: For persons and transactions subject to the electronic invoicing regime. Do not assume every business already has the same deadline.
Source I:AE-INVOICE: FTA calls on persons subject to electronic invoicing to comply with deadlines <https://tax.gov.ae/en/media.centre/News/federal.tax.authority.calls.on.persons.subject.to.einvoicing.to.comply.wit.the.prescribed.legal.deadlines.and.avoid.administrative.penalties.aspx>. Checked 2026-11-03. Latest accessed notice differs from older appointment deadline. No thresholds or universal immediate obligation asserted.

procurement_payment | scope SA | legal: Saudi Arabia: ZATCA distinguishes invoice generation requirements from integration requirements introduced in notified waves. Ask finance which phase and notice apply.
Applies only: For taxpayers and invoices within the electronic invoicing rules; nonresident and other exclusions require checking.
Source I:SA-INVOICE: Electronic invoice rollout phases <https://zatca.gov.sa/en/E-Invoicing/Introduction/Pages/Roll-out-phases.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. No universal integration deadline, tax rate or revenue threshold asserted.

data_privacy | scope AE | legal: UAE: Federal Decree Law 45 of 2021 on personal data has exclusions, including certain sector data and free zones with their own privacy laws. Identify the entity, data and legal regime before choosing controls.
Applies only: Apply only after checking Article 2 exclusions and the relevant implementation instruments. Do not infer DIFC or ADGM from a city name.
Source I:AE-PDPL: Federal Decree Law 45 of 2021 concerning the Protection of Personal Data <https://www.uaelegislation.gov.ae/en/legislations/1972/download>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Current executive instruments and implementation timing must be checked. No universal federal privacy or residency claim.

data_privacy | scope SA | legal: Saudi Arabia: the Personal Data Protection Law and the Regulation on Personal Data Transfer outside the Kingdom require an applicable transfer basis and protection review. Map overseas processing before agreeing the contract.
Applies only: For personal data transfers within the Saudi regime. This is not a blanket requirement to keep every type of data in Saudi Arabia.
Source I:SA-TRANSFER: Regulation on Personal Data Transfer outside the Kingdom <https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/details/PDPL2/!ut/p/z0/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziPR1dzTwMgw2MDMOcTA3MjH39TE29jY0MQsz1g1Pz9L30o_ArAppiVOTr7JuuH1WQWJKhm5mXlq8fEeAS4GOkX5DtHg4A45XaIQ!!/>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Read with Personal Data Protection Law and implementing regulations; no blanket local hosting requirement inferred.

buyer_language | scope COMMON | question: Which languages must the buying team, users, contract and notices support?

proof | scope COMMON | question: What sample workflow and acceptance evidence will the buyer approve?

objections | scope COMMON | question: Which hosting, access, integration, support or contract issue could block this purchase?

sales_motion | scope COMMON | question: Who owns the evaluation, acceptance decision and next purchase step?

### logistics-tech | inherited | inherits defaults
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### fintech | waiting_for_source | inherits defaults
Inherit only applicable parent notes and add the country and activity specific differences below.
Waiting for a source: Complete country source coverage outside the explicitly sourced notes.

sector_regulator | scope AE | legal: UAE: Federal Decree Law 6 of 2025 covers CBUAE licensed financial activities. Confirm the entity and whether a financial free zone regime applies before selecting obligations.
Applies only: For financial institutions and activities within the federal law; do not assume every UAE buyer is in its scope.
Source I:AE-CBUAE: Federal Decree Law 6 of 2025 regarding the Central Bank, Regulation of Financial Institutions and Activities, and Insurance Business <https://mof.gov.ae/wp-content/uploads/2025/11/Federal-Decree-Law-No.-6-of-2025-Regarding-the-Central-Bank-Regulation-of-Financial-Institutions-and-Activities-and-Insurance-Business.pdf>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Exact release date not established from the PDF excerpt. Financial free zone scope and activity exclusions require checking. No licence conclusion for vendors.

sector_regulator | scope AE | legal: If the activity is conducted in or from DIFC, check the Dubai Financial Services Authority regime with the contracting entity.
Applies only: DIFC financial activity only. Dubai city alone does not establish this scope.
Source I:AE-DFSA: About the DFSA <https://www.dfsa.ae/about-dfsa/who-we-are/the-dfsa>. Checked 2026-11-03. No reliable full publication date on the retrieved page. DIFC only. Dubai city does not establish DIFC jurisdiction.

sector_regulator | scope AE | legal: If the financial activity is in ADGM, check the Financial Services Regulatory Authority regime with the contracting entity.
Applies only: ADGM financial activity only. Abu Dhabi city alone does not establish this scope.
Source I:AE-FSRA: Financial Services Regulatory Authority <https://www.adgm.com/financial-services-regulatory-authority>. Checked 2026-11-03. No reliable full publication date on the retrieved page. ADGM only. Abu Dhabi city does not establish ADGM jurisdiction.

sector_regulator | scope SA | legal: Saudi Arabia: the Saudi Central Bank Law gives SAMA supervisory powers over financial institutions within relevant sector laws. Identify the activity and actual regulated entity.
Applies only: For financial institutions in SAMA's remit. Insurance and securities activities have separate subtype checks.
Source I:SA-SAMA: Saudi Central Bank Law <https://sama.gov.sa/en-US/About/Pages/bank-law.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Relevant sector laws determine the entity scope. Insurance remit is separately mapped to the Insurance Authority.

### vertical-saas | inherited | inherits defaults
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### ai-native | inherited | inherits defaults
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### ites | inherited | inherits defaults
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### telecom | waiting_for_source | inherits defaults
Inherit only applicable parent notes and add the country and activity specific differences below.
Waiting for a source: Complete country source coverage outside the explicitly sourced notes.

sector_regulator | scope AE | legal: UAE: TDRA issues licences for public telecommunications networks and services under the Telecommunications Law. Distinguish operating the service from supplying an operator.
Applies only: For activities requiring TDRA authorisation, not every telecom software supplier.
Source I:AE-TELECOM: Issue licences to provide telecommunication services <https://tdra.gov.ae/en/Services/issue-licences-to-provide-telecommunication-services>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Not a requirement for every software vendor supplying an operator.

### cybersecurity | waiting_for_source | inherits defaults
Inherit only applicable parent notes and add the country and activity specific differences below.
Waiting for a source: Complete country source coverage outside the explicitly sourced notes.

sector_regulator | scope SA | legal: Saudi Arabia: NCA publishes Essential Cybersecurity Controls ECC 2 2024. Ask the buyer which entity and system scope applies before mapping the proposed controls.
Applies only: For an entity and system within the controls' scope. This note does not claim every private buyer is subject to every NCA control.
Source I:SA-ECC: Essential Cybersecurity Controls ECC 2 2024 <https://nca.gov.sa/en/regulatory-documents/controls-list/ecc/>. Checked 2026-11-03. Date is official page publication. No blanket all private business mandate or detailed control asserted; scope must be established.

### software | inherited | inherits defaults
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### saas | specific | inherits defaults
Inherit only applicable parent notes and add the country and activity specific differences below.

sector_regulator | scope SA | legal: Saudi Arabia: CST's Cloud Computing Service Provisioning Regulations replace the older Cloud Computing Regulatory Framework. Check whether the offered service is within that regime.
Applies only: Only if the actual service is covered by the cloud regulations; do not infer registration solely from the SaaS label.
Source I:SA-CLOUD: Cloud Computing Service Provisioning Regulations and guides decision 506/1445 <https://www.cst.gov.sa/en/regulations-and-licenses/decisions/Regulation-1482>. Checked 2026-11-03. Used for current instrument naming only. Cloud service classification and registration require separate review.

### freight-visibility | inherited | inherits logistics-tech
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### freight-marketplace | inherited | inherits logistics-tech
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### seller-shipping | inherited | inherits logistics-tech
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### last-mile | inherited | inherits logistics-tech
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### warehousing | inherited | inherits logistics-tech
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### transport-management | inherited | inherits logistics-tech
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### payments-banking | waiting_for_source | inherits fintech
Inherit only applicable parent notes and add the country and activity specific differences below.
Waiting for a source: Complete this activity's sources for Qatar, Bahrain, Oman and Kuwait.

sector_regulator | scope AE | legal: UAE: the CBUAE law lists payment, stored value and related licensed financial activities. Map the money flow and provider role before selecting the licensing route.
Applies only: For activities within Article 61 and applicable regulations, subject to financial free zone scope.
Source I:AE-CBUAE: Federal Decree Law 6 of 2025 regarding the Central Bank, Regulation of Financial Institutions and Activities, and Insurance Business <https://mof.gov.ae/wp-content/uploads/2025/11/Federal-Decree-Law-No.-6-of-2025-Regarding-the-Central-Bank-Regulation-of-Financial-Institutions-and-Activities-and-Insurance-Business.pdf>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Exact release date not established from the PDF excerpt. Financial free zone scope and activity exclusions require checking. No licence conclusion for vendors.

sector_regulator | scope SA | legal: Saudi Arabia: Article 7 of the Law of Payments and Payment Services assigns payment oversight and licensing powers to SAMA. Identify the operator or provider role.
Applies only: For payment systems and services in the law's scope.
Source I:SA-PAYMENTS: Law of Payments and Payment Services: Article 7 <https://www.rulebook.sama.gov.sa/en/article-7-24>. Checked 2026-11-03. Use with current implementing regulations; no assertion that every software supplier is a payment provider.

### core-banking | inherited | inherits fintech
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### lending | waiting_for_source | inherits fintech
Inherit only applicable parent notes and add the country and activity specific differences below.
Waiting for a source: Complete this activity's sources for Qatar, Bahrain, Oman and Kuwait.

decision_approvers | scope SA | legal: Saudi Arabia: SAMA's finance company compliance and internal audit principles address board and executive responsibilities. Ask the finance company to name its accountable reviewers.
Applies only: For finance and real estate refinance companies within the named principles.
Source I:SA-FINANCE: Compliance and internal audit principles for finance companies <https://sama.gov.sa/en-us/mediacenter/news/pages/news-1044.aspx>. Checked 2026-11-03. Primary indexed official notice read; live open timed out. Only the named finance and refinance company categories.

sector_regulator | scope AE | legal: UAE: credit and funding facilities are licensed activities under the CBUAE law. Confirm the lender's entity and jurisdiction before choosing the approval path.
Applies only: For activities within the federal law; do not apply this as a licence requirement for all lending software.
Source I:AE-CBUAE: Federal Decree Law 6 of 2025 regarding the Central Bank, Regulation of Financial Institutions and Activities, and Insurance Business <https://mof.gov.ae/wp-content/uploads/2025/11/Federal-Decree-Law-No.-6-of-2025-Regarding-the-Central-Bank-Regulation-of-Financial-Institutions-and-Activities-and-Insurance-Business.pdf>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Exact release date not established from the PDF excerpt. Financial free zone scope and activity exclusions require checking. No licence conclusion for vendors.

### wealth-investment | waiting_for_source | inherits fintech
Inherit only applicable parent notes and add the country and activity specific differences below.
Waiting for a source: Complete this activity's sources for Qatar, Bahrain, Oman and Kuwait.

sector_regulator | scope AE | legal: UAE: Federal Decree Law 32 of 2025 establishes the Capital Market Authority framework. Confirm whether the activity is under this regime or a financial free zone regulator.
Applies only: For UAE capital market activities in the federal authority's remit; separate DIFC and ADGM scope must be checked.
Source I:AE-CMA: Federal Decree Law 32 of 2025 regarding Capital Market Authority <https://legislation.uaecma.gov.ae/en/capital-market-authority-law>. Checked 2026-11-03. Date is official gazette date. Primary indexed entry read; live open timed out. Do not conflate this authority with the Saudi authority of the same English name.

sector_regulator | scope SA | legal: Saudi Arabia: the Capital Market Authority regulates securities activities under the Capital Market Law. Identify the investment service and entity before selecting obligations.
Applies only: For Saudi capital market activity. This is the Saudi authority.
Source I:SA-CMA: Frequently asked questions for implementing regulations <https://cma.gov.sa/en/RulesRegulations/FAQ/Pages/FAQs.aspx>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Do not confuse with the UAE Capital Market Authority.

### spend-expense | inherited | inherits fintech
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### insurance | waiting_for_source | inherits fintech
Inherit only applicable parent notes and add the country and activity specific differences below.
Waiting for a source: Complete this activity's sources for Qatar, Bahrain, Oman and Kuwait.

sector_regulator | scope AE | legal: UAE: the CBUAE law includes insurance and reinsurance activities. Establish whether the insurer is under the federal regime or a financial free zone regime.
Applies only: For the insurance activity and entity in scope; separate DIFC and ADGM conditions remain conditional.
Source I:AE-CBUAE: Federal Decree Law 6 of 2025 regarding the Central Bank, Regulation of Financial Institutions and Activities, and Insurance Business <https://mof.gov.ae/wp-content/uploads/2025/11/Federal-Decree-Law-No.-6-of-2025-Regarding-the-Central-Bank-Regulation-of-Financial-Institutions-and-Activities-and-Insurance-Business.pdf>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Exact release date not established from the PDF excerpt. Financial free zone scope and activity exclusions require checking. No licence conclusion for vendors.

sector_regulator | scope SA | legal: Saudi Arabia: the Insurance Authority is the insurance regulator and sets insurance licensing requirements. Use the insurer or intermediary's current regulatory category.
Applies only: For insurance activity in Saudi Arabia within the Authority's remit.
Source I:SA-INSURANCE: About the Insurance Authority <https://www.ia.gov.sa/en/about-ia/about>. Checked 2026-11-03. No reliable full publication date on the retrieved page. Do not use the older SAMA insurance supervision attribution. Current product regulations still need scope checks.

### customer-service | inherited | inherits saas
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### crm-marketing | inherited | inherits saas
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### collaboration | inherited | inherits saas
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### product-growth | inherited | inherits saas
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### construction | inherited | inherits vertical-saas
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### property-management | inherited | inherits vertical-saas
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### field-services | inherited | inherits vertical-saas
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### fmcg-retail-execution | inherited | inherits vertical-saas
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### industry-hr-payroll | inherited | inherits vertical-saas
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### hotel-lodging | inherited | inherits vertical-saas
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### retail-restaurant-ops | inherited | inherits vertical-saas
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### agents-copilots | inherited | inherits ai-native
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### voice-language-models | inherited | inherits ai-native
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### enterprise-search | inherited | inherits ai-native
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### it-services | inherited | inherits ites
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### bpo-cx | inherited | inherits ites
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### digital-engineering | inherited | inherits ites
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### data-services | inherited | inherits ites
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### operators-connectivity | inherited | inherits telecom
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### cpaas-messaging | inherited | inherits telecom
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### telecom-software | inherited | inherits telecom
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### business-voice-ucaas | inherited | inherits telecom
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### developer-platform | inherited | inherits software
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### data-infrastructure | inherited | inherits software
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### observability | inherited | inherits software
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### testing | inherited | inherits software
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### dev-tools | inherited | inherits software
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### cloud-security | inherited | inherits cybersecurity
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### identity-security | inherited | inherits cybersecurity
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### email-security | inherited | inherits cybersecurity
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### awareness-training | inherited | inherits cybersecurity
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### appsec | inherited | inherits cybersecurity
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### mobile-appsec | inherited | inherits cybersecurity
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### soc-services | inherited | inherits cybersecurity
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### endpoint-network | inherited | inherits cybersecurity
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### document-ai | inherited | inherits ai-native
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### ai-video | inherited | inherits ai-native
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### engineering-talent | inherited | inherits ites
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### product-management | inherited | inherits saas
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### digital-adoption | inherited | inherits saas
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### pentest | inherited | inherits cybersecurity
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### attack-surface-dast | inherited | inherits cybersecurity
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### process-orchestration | inherited | inherits software
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### open-source-support | inherited | inherits software
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

### iot-connectivity | inherited | inherits telecom
No validated additional override was established for this cell in the sourced countries. Inherit only notes for the named country; other countries remain outside factual coverage.

## UK

United Kingdom only. Check the relevant UK nation for devolved procurement and transport rules. Country selection does not establish that a buyer or product is regulated. Draft for owner review.
Countries: GB = United Kingdom
Clues, only in selling context: {"aliases":["UK","United Kingdom"],"countries":[{"code":"GB","name":"United Kingdom","aliases":["UK","United Kingdom","Britain","Great Britain","England","Scotland","Wales","Northern Ireland"],"cities":["London","Manchester","Birmingham","Edinburgh","Cardiff","Belfast"],"currencies":["GBP","pound sterling"],"regulators":["Financial Conduct Authority","Prudential Regulation Authority","Ofcom","Information Commissioner's Office"]}]}

### Defaults

decision_approvers | scope GB | question: Who owns the budget, accepts the operational risk and approves the handling of personal data for this UK purchase?

procurement_payment | scope GB | question: Is this a public tender, a framework purchase or a private contract, and what are the agreed invoice currency, acceptance steps and payment terms?

data_privacy | scope GB | legal: For UK GDPR processing on a controller's behalf, prepare the Article 28 contract, subprocessor approvals and data return or deletion terms before exchanging personal data.
Applies only: Where UK GDPR applies and the supplier is a processor; first establish the parties' actual roles.
Source J:UK-ICO-CONTRACT: Contracts <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/guide-to-accountability-and-governance/contracts/>. Checked 2026-11-03. Publication date not reliably shown. Primary source text retrieved in search; direct fetch returned 403. Applies only to controller and processor processing within UK GDPR scope.

buyer_language | scope GB | question: Which language and terminology does the buying team require for the proposal, training and support?

proof | scope GB | question: What buyer approved evidence and acceptance test will show that this purchase solves the stated problem?

objections | scope GB | question: Which unresolved issue could stop approval: security, implementation effort, accountability, contract terms or proof of value?

sales_motion | scope GB | question: Who must agree the pilot scope, success criteria and route to a paid contract before work starts?

### logistics-tech | specific | inherits defaults
Parent context remains. The following sourced UK addition applies only within its stated scope.

proof | scope GB | legal: For a covered road transport operation, demonstrate how scheduling and record exports help the operator meet the drivers' hours and tachograph duties described by DVSA.
Applies only: Confirm vehicle, route and exemptions first. The cited guidance must not be assumed to establish Northern Ireland requirements.
Source J:UK-DVSA-HOURS: Drivers' hours and tachographs: responsibilities of vehicle operators <https://www.gov.uk/guidance/drivers-hours-goods-vehicles/5-responsibilities-of-vehicle-operators>. Checked 2026-11-03. Updated 2026-07-01. Confirm vehicle, route, exemptions and Great Britain versus Northern Ireland scope before use.

### fintech | specific | inherits defaults
Parent context remains. The following sourced UK addition applies only within its stated scope.

sector_regulator | scope GB | legal: FCA SYSC outsourcing requirements vary by firm and function. Classify the arrangement with the regulated buyer; a standard software purchase is not automatically outsourcing.
Applies only: For UK firms within the relevant FCA rules; test the service against the applicable outsourcing definition.
Source J:UK-FCA-OUTSOURCE: Outsourcing and operational resilience <https://www.fca.org.uk/firms/outsourcing-and-operational-resilience>. Checked 2026-11-03. Updated 2026-07-14. Future reporting rules from 2027 are not treated as current. Buying standard software is not automatically outsourcing.

proof | scope GB | legal: Where the service is outsourced, show the buyer its dependencies, security controls and exit approach. The regulated firm retains responsibility for managing third party risk.
Applies only: For arrangements within the buyer's applicable FCA outsourcing and risk management obligations.
Source J:UK-FCA-OUTSOURCE: Outsourcing and operational resilience <https://www.fca.org.uk/firms/outsourcing-and-operational-resilience>. Checked 2026-11-03. Updated 2026-07-14. Future reporting rules from 2027 are not treated as current. Buying standard software is not automatically outsourcing.

### vertical-saas | inherited | inherits defaults
Reviewed against the sourced UK defaults. No distinct sector override has been validated; use defaults. This is not a finding that the sector has no additional obligations.

### ai-native | specific | inherits defaults
Parent context remains. The following sourced UK addition applies only within its stated scope.

data_privacy | scope GB | legal: Use the ICO AI guidance to examine risks to individuals when UK personal data enters an AI workflow. Distinguish legal duties from recommended practice; the guidance is under review and is not a statutory code.
Applies only: For AI processing within UK data protection scope; verify current guidance before relying on a particular automated decision rule.
Source J:UK-ICO-AI: About this guidance: AI and data protection <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/about-this-guidance/>. Checked 2026-11-03. No reliable publication date shown. Guidance is under review following the Data (Use and Access) Act; it is not a statutory code.

### ites | inherited | inherits defaults
Reviewed against the sourced UK defaults. No distinct sector override has been validated; use defaults. This is not a finding that the sector has no additional obligations.

### telecom | specific | inherits defaults
Parent context remains. The following sourced UK addition applies only within its stated scope.

sector_regulator | scope GB | legal: Ofcom's General Conditions of Entitlement operate under the Communications Act 2003. Identify the network or service being supplied and the providers covered by each relevant condition.
Applies only: For provision of UK electronic communications networks or services; supplying software to an operator does not by itself establish provider status.
Source J:UK-OFCOM-GC: General Conditions of Entitlement <https://www.ofcom.org.uk/phones-and-broadband/accessibility/general-conditions-of-entitlement>. Checked 2026-11-03. Updated 2026-04-08. Each condition has its own regulated provider definition; not all software sellers are communications providers.

### cybersecurity | specific | inherits defaults
Parent context remains. The following sourced UK addition applies only within its stated scope.

procurement_payment | scope GB | legal: For a qualifying public contract, map the tender's security evidence to PPN 014. It allows Cyber Essentials, Cyber Essentials Plus or equivalent controls; it does not impose certification on every UK purchase.
Applies only: Only for the bodies and contract risks identified in PPN 014. Confirm the actual tender and procurement commencement date.
Source J:UK-CABINET-CYBER: PPN 014: Cyber essentials scheme <https://www.gov.uk/government/publications/ppn-014-cyber-essentials-scheme/ppn-014-cyber-essentials-scheme-html>. Checked 2026-11-03. Applies to stated central government and NHS bodies and qualifying contracts, not all UK procurement. No blanket certification requirement.

### software | inherited | inherits defaults
Reviewed against the sourced UK defaults. No distinct sector override has been validated; use defaults. This is not a finding that the sector has no additional obligations.

### saas | inherited | inherits defaults
Reviewed against the sourced UK defaults. No distinct sector override has been validated; use defaults. This is not a finding that the sector has no additional obligations.

### freight-visibility | inherited | inherits logistics-tech
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### freight-marketplace | inherited | inherits logistics-tech
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### seller-shipping | inherited | inherits logistics-tech
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### last-mile | inherited | inherits logistics-tech
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### warehousing | inherited | inherits logistics-tech
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### transport-management | inherited | inherits logistics-tech
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### payments-banking | specific | inherits fintech
Parent context remains. The following sourced UK addition applies only within its stated scope.

sector_regulator | scope GB | legal: Separate payment services from electronic money issuance. The FCA explains authorisation and registration under the Payment Services Regulations 2017 and Electronic Money Regulations 2011, with exclusions and existing provider exceptions.
Applies only: Where the firm's own activities fall within UK payment or electronic money regulation; an API supplier is not automatically a regulated provider.
Source J:UK-FCA-PAYMENTS: Payment Services Regulations 2017 and Electronic Money Regulations 2011 <https://www.fca.org.uk/firms/payment-services-regulations-e-money-regulations>. Checked 2026-11-03. Updated 2025-12-17. Technical suppliers are not automatically payment institutions.

### core-banking | specific | inherits fintech
Parent context remains. The following sourced UK addition applies only within its stated scope.

sector_regulator | scope GB | legal: A new UK bank applies to the Prudential Regulation Authority. Establish whether the prospect is the regulated institution or its technology supplier before assigning banking approval work.
Applies only: Where the activity involves establishing a bank; this is not a licence requirement for ordinary core banking software supply.
Source J:UK-PRA-AUTH: New firm authorisation <https://www.bankofengland.co.uk/prudential-regulation/Authorisations/new-firm-authorisation>. Checked 2026-11-03. Publication date not shown. Not a claim that software providers need a banking or insurance authorisation.

### lending | specific | inherits fintech
Parent context remains. The following sourced UK addition applies only within its stated scope.

proof | scope GB | legal: For regulated consumer lending, the FCA expects evidence showing how credit risk, affordability and customers in financial difficulty are handled. Demonstrate the relevant decision and escalation workflow.
Applies only: For consumer credit activities within the FCA's authorisation scope; do not extend automatically to all commercial credit or software vendors.
Source J:UK-FCA-CREDIT: Apply to become a consumer credit lender or hirer <https://www.fca.org.uk/firms/authorisation/consumer-credit-lenders-hirers>. Checked 2026-11-03. Updated 2024-09-17. Consumer activity scope; do not apply automatically to commercial lending.

### wealth-investment | specific | inherits fintech
Parent context remains. The following sourced UK addition applies only within its stated scope.

sector_regulator | scope GB | legal: Use the FCA application category for the actual consumer investment activity, such as financial advice, wealth management, stockbroking or operating an investment platform.
Applies only: Where the firm's own UK investment activity requires authorisation; a software product label does not determine permission.
Source J:UK-FCA-WEALTH: Authorisation <https://www.fca.org.uk/firms/authorisation>. Checked 2026-11-03. Publication date not established. Directory supports regulator routing, not a complete account of permissions or exemptions.

### spend-expense | specific | inherits fintech
Parent context remains. The following sourced UK addition applies only within its stated scope.

sector_regulator | scope GB | legal: If an expense product also executes payments or issues electronic money, assess those activities against the Payment Services Regulations 2017 or Electronic Money Regulations 2011 before promising a regulated service.
Applies only: Only where the actual service includes an in scope payment or electronic money activity; expense record keeping alone does not establish that scope.
Source J:UK-FCA-PAYMENTS: Payment Services Regulations 2017 and Electronic Money Regulations 2011 <https://www.fca.org.uk/firms/payment-services-regulations-e-money-regulations>. Checked 2026-11-03. Updated 2025-12-17. Technical suppliers are not automatically payment institutions.

### insurance | specific | inherits fintech
Parent context remains. The following sourced UK addition applies only within its stated scope.

sector_regulator | scope GB | legal: Distinguish an insurer from an insurance intermediary. New insurers apply to the Prudential Regulation Authority; the FCA lists a separate authorisation route for general insurance intermediaries.
Applies only: For authorisation of the relevant UK insurance business; do not treat an insurer's software supplier as the insurer.
Source J:UK-PRA-AUTH: New firm authorisation <https://www.bankofengland.co.uk/prudential-regulation/Authorisations/new-firm-authorisation>. Checked 2026-11-03. Publication date not shown. Not a claim that software providers need a banking or insurance authorisation.
Source J:UK-FCA-WEALTH: Authorisation <https://www.fca.org.uk/firms/authorisation>. Checked 2026-11-03. Publication date not established. Directory supports regulator routing, not a complete account of permissions or exemptions.

### customer-service | inherited | inherits saas
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### crm-marketing | inherited | inherits saas
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### collaboration | inherited | inherits saas
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### product-growth | inherited | inherits saas
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### construction | inherited | inherits vertical-saas
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### property-management | inherited | inherits vertical-saas
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### field-services | inherited | inherits vertical-saas
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### fmcg-retail-execution | inherited | inherits vertical-saas
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### industry-hr-payroll | specific | inherits vertical-saas
Parent context remains. The following sourced UK addition applies only within its stated scope.

proof | scope GB | legal: For UK PAYE payroll, demonstrate the Full Payment Submission sent to HM Revenue and Customs on or before payday, with a controlled correction process.
Applies only: For employers reporting PAYE payroll; check permitted reporting exceptions for the actual circumstances.
Source J:UK-HMRC-PAYROLL: Running payroll: Reporting to HMRC: FPS <https://www.gov.uk/running-payroll/reporting-to-hmrc>. Checked 2026-11-03. Publication date not shown. PAYE payroll and reporting exceptions must be checked for the employer.

### hotel-lodging | inherited | inherits vertical-saas
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### retail-restaurant-ops | inherited | inherits vertical-saas
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### agents-copilots | inherited | inherits ai-native
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### voice-language-models | inherited | inherits ai-native
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### enterprise-search | inherited | inherits ai-native
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### it-services | inherited | inherits ites
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### bpo-cx | inherited | inherits ites
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### digital-engineering | inherited | inherits ites
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### data-services | inherited | inherits ites
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### operators-connectivity | inherited | inherits telecom
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### cpaas-messaging | inherited | inherits telecom
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### telecom-software | inherited | inherits telecom
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### business-voice-ucaas | specific | inherits telecom
Parent context remains. The following sourced UK addition applies only within its stated scope.

proof | scope GB | legal: For a covered UK voice service, test emergency access and caller location handling against Ofcom General Condition A3 rather than presenting ordinary call availability as sufficient.
Applies only: Only for providers and services within the condition's scope; confirm the service classification.
Source J:UK-OFCOM-GC: General Conditions of Entitlement <https://www.ofcom.org.uk/phones-and-broadband/accessibility/general-conditions-of-entitlement>. Checked 2026-11-03. Updated 2026-04-08. Each condition has its own regulated provider definition; not all software sellers are communications providers.

### developer-platform | inherited | inherits software
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### data-infrastructure | inherited | inherits software
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### observability | inherited | inherits software
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### testing | inherited | inherits software
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### dev-tools | inherited | inherits software
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### cloud-security | inherited | inherits cybersecurity
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### identity-security | inherited | inherits cybersecurity
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### email-security | inherited | inherits cybersecurity
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### awareness-training | inherited | inherits cybersecurity
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### appsec | inherited | inherits cybersecurity
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### mobile-appsec | inherited | inherits cybersecurity
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### soc-services | inherited | inherits cybersecurity
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### endpoint-network | inherited | inherits cybersecurity
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### document-ai | inherited | inherits ai-native
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### ai-video | inherited | inherits ai-native
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### engineering-talent | inherited | inherits ites
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### product-management | inherited | inherits saas
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### digital-adoption | inherited | inherits saas
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### pentest | inherited | inherits cybersecurity
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### attack-surface-dast | inherited | inherits cybersecurity
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### process-orchestration | inherited | inherits software
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### open-source-support | inherited | inherits software
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

### iot-connectivity | inherited | inherits telecom
No validated UK difference beyond the parent vertical and defaults; inherit those notes. This is not a complete regulatory assessment of the buyer.

## Western Europe

This draft covers Austria, Belgium, France, Germany, Liechtenstein, Luxembourg, Monaco, the Netherlands and Switzerland. The UK has its own file. This is a declared country scope, not a claim that all European markets are covered. EU provisions are attached only to the listed EU countries when that territorial scope is sourced. Liechtenstein, Monaco and Switzerland receive separately sourced notes. No country is a regional default. Draft for owner review.
Countries: AT = Austria (EU member); BE = Belgium (EU member); FR = France (EU member); DE = Germany (EU member); LI = Liechtenstein; LU = Luxembourg (EU member); MC = Monaco; NL = Netherlands (EU member); CH = Switzerland
Clues, only in selling context: {"aliases":["Western Europe"],"countries":[{"code":"AT","name":"Austria","aliases":["Austria","Österreich"],"cities":["Vienna"],"currencies":[],"regulators":["Finanzmarktaufsicht"]},{"code":"BE","name":"Belgium","aliases":["Belgium","Belgique","België"],"cities":["Brussels"],"currencies":[],"regulators":["National Bank of Belgium"]},{"code":"FR","name":"France","aliases":["France"],"cities":["Paris","Lyon"],"currencies":[],"regulators":["Autorité de contrôle prudentiel et de résolution","Arcep"]},{"code":"DE","name":"Germany","aliases":["Germany","Deutschland"],"cities":["Berlin","Frankfurt","Munich"],"currencies":[],"regulators":["BaFin","Bundesnetzagentur"]},{"code":"LI","name":"Liechtenstein","aliases":["Liechtenstein"],"cities":["Vaduz"],"currencies":[],"regulators":["Financial Market Authority Liechtenstein"]},{"code":"LU","name":"Luxembourg","aliases":["Luxembourg"],"cities":[],"currencies":[],"regulators":["Commission de Surveillance du Secteur Financier"]},{"code":"MC","name":"Monaco","aliases":["Monaco"],"cities":[],"currencies":[],"regulators":["Commission de Contrôle des Activités Financières"]},{"code":"NL","name":"Netherlands","aliases":["Netherlands","Nederland"],"cities":["Amsterdam","Rotterdam"],"currencies":[],"regulators":["De Nederlandsche Bank"]},{"code":"CH","name":"Switzerland","aliases":["Switzerland","Schweiz","Suisse","Svizzera"],"cities":["Zurich","Geneva","Bern"],"currencies":[],"regulators":["FINMA","Federal Data Protection and Information Commissioner"]}]}

### Defaults

decision_approvers | scope COMMON | question: Which country and legal entity will buy, and who approves the budget, operational risk and data processing?

procurement_payment | scope COMMON | question: What tender or contracting route, invoice currency, acceptance process and payment terms has this buyer specified?

data_privacy | scope AT,BE,FR,DE,LU,NL | legal: For the listed EU countries, establish controller and processor roles under the General Data Protection Regulation. Put the processing contract and written subprocessor authorisation in place before personal data is shared.
Applies only: Only for processing within GDPR territorial and material scope; determine the parties' roles for each processing purpose.
Source J:EU-GDPR: Data controller or data processor <https://www.edpb.europa.eu/sme/learn-the-basics/data-controller-or-data-processor_en>. Checked 2026-11-03. Publication date not shown. Territorial scope and actual processing role must be established.

data_privacy | scope CH | legal: Switzerland: under Article 9 of the Federal Act on Data Protection, check processor instructions, confidentiality and security, and obtain controller approval before further outsourcing.
Applies only: For processing within Swiss FADP scope. Separately check the countries of processing and any cross border disclosure.
Source J:CH-FADP: Outsourcing of data processing <https://www.edoeb.admin.ch/en/outsourcing-of-data-processing>. Checked 2026-11-03. Publication date not shown. Swiss law; cross border disclosure requires a separate assessment.

data_privacy | scope LI | legal: Liechtenstein: the Datenschutzstelle explains that an Article 28 GDPR contract must define the processing and the controller's and processor's respective duties.
Applies only: For a controller and processor relationship subject to GDPR in Liechtenstein; this does not establish the scope of other EU instruments.
Source J:LI-GDPR: Verantwortlicher <https://www.datenschutzstelle.li/datenschutz/themen-z/verantwortlicher>. Checked 2026-11-03. Publication date not shown. German primary guidance; do not infer applicability of other EU legislation from GDPR.

data_privacy | scope MC | legal: Monaco: Article 26 of Loi n° 1.565 du 3 décembre 2024 requires a written processor contract specifying the processing and the parties' obligations.
Applies only: For personal data processing subject to Monaco's law and a genuine controller and processor relationship.
Source J:MC-APDP: Questions fréquentes <https://apdp.mc/faq/>. Checked 2026-11-03. Publication date not shown. Monaco law; not an assertion of EU GDPR territorial coverage.

buyer_language | scope COMMON | question: Which language does each country's buying team require for the proposal, implementation, evidence and support?

proof | scope COMMON | question: Which buyer approved workflow and acceptance test would demonstrate value in the named country?

objections | scope COMMON | question: Which unresolved requirement could stop approval in this country, and whose evidence will settle it?

sales_motion | scope COMMON | question: Who owns the local pilot and the decision to proceed to a paid contract?

### logistics-tech | specific | inherits defaults
Use applicable parent notes and these additions only for their named countries and activities.

proof | scope AT,BE,FR,DE,LU,NL | legal: In the listed EU countries, test the road operator's workflow against Regulation (EC) No 561/2006, including the relevant vehicle and route scope and any national derogation.
Applies only: For covered road transport operations, not every logistics software workflow. Confirm the national exception rather than importing another country's.
Source J:EU-ROAD: Driving time and rest periods <https://transport.ec.europa.eu/transport-modes/road/social-provisions/driving-time-and-rest-periods_en>. Checked 2026-11-03. Publication date not shown. Vehicle and route scope plus national derogations matter; no blanket rule for all logistics software.

### fintech | specific | inherits defaults
Use applicable parent notes and these additions only for their named countries and activities.

decision_approvers | scope AT,BE,FR,DE,LU,NL | legal: DORA requires the financial entity to assess ICT provider risk before contracting. Identify the buyer's accountable risk reviewer and supply evidence for that assessment.
Applies only: For the covered entity's third party ICT risk process; this does not classify every supplier as a designated critical provider.
Source J:EU-DORA: Regulation (EU) 2022/2554 on digital operational resilience for the financial sector <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554>. Checked 2026-11-03. Read primary legal text in indexed search. Direct ELI view served a JavaScript challenge. Apply only to financial entities and arrangements within scope; not every technology supplier is directly supervised.

sector_regulator | scope CH | legal: Switzerland: FINMA has different authorisation routes for banking, securities, insurance and asset management. Start with the actual financial activity and legal entity.
Applies only: Where Swiss financial market law requires a permit, registration or other authorisation; ordinary technology supply alone does not establish that requirement.
Source J:CH-FINMA: Authorisation to operate in the financial market <https://www.finma.ch/en/authorisation/authorisation-overview/>. Checked 2026-11-03. Publication date not shown. Activity specific permits, registration or self regulatory organisation routes; no blanket fintech licence.

sector_regulator | scope LI | legal: Liechtenstein: the Financial Market Authority lists separate licensing routes for banks, investment firms, payment institutions and electronic money institutions. Confirm the activity before using a route.
Applies only: For an institution undertaking the relevant regulated activity in Liechtenstein, not solely a technology supplier.
Source J:LI-FMA: Financial Institutions Division <https://www.fma-li.li/en/financial-intermediaries/financial-institutions-division>. Checked 2026-11-03. Publication date not shown. Directory establishes routes, not complete substantive permissions.

sector_regulator | scope MC | legal: Monaco: financial activities under Act No. 1.338 require the relevant CCAF authorisation and a separate government business approval. Credit institution status also involves ACPR authorisation.
Applies only: Only for the financial activities and institutions covered by the cited formalities; do not extend this route to every fintech business.
Source J:MC-CCAF: Formalities for carrying out a financial activity <https://ccaf.mc/en/authorised-firms/carrying-out-a-financial-activity/formalities/>. Checked 2026-11-03. Publication date not shown. CCAF financial activity scope, not a general licence for all insurance or payment services.

procurement_payment | scope AT,BE,FR,DE,LU,NL | legal: For an EU financial entity within Regulation (EU) 2022/2554, DORA, prepare the ICT service description, processing locations, subcontracting terms and exit evidence needed for the buyer's contract review.
Applies only: For financial entities and ICT arrangements within DORA scope; identify whether a critical or important function is supported.
Source J:EU-DORA: Regulation (EU) 2022/2554 on digital operational resilience for the financial sector <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554>. Checked 2026-11-03. Read primary legal text in indexed search. Direct ELI view served a JavaScript challenge. Apply only to financial entities and arrangements within scope; not every technology supplier is directly supervised.

### vertical-saas | inherited | inherits defaults
Reviewed against the country scoped defaults. No separately validated sector addition; inherit only defaults applicable to the named country. This is not an exhaustive regulatory inventory.

### ai-native | specific | inherits defaults
Use applicable parent notes and these additions only for their named countries and activities.

proof | scope AT,BE,FR,DE,LU,NL | legal: For the listed EU markets, classify the provider or deployer role under the AI Act and demonstrate the Article 50 transparency measures that apply to the actual system.
Applies only: For AI systems within the Act's scope. Check the relevant paragraph, exceptions and transition before stating a duty or date.
Source J:EU-AI: Transparency obligations under Article 50 of the AI Act <https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act>. Checked 2026-11-03. Publication date not shown. Check the exact paragraph and transition; do not treat all AI obligations as applying on one date.

### ites | inherited | inherits defaults
Reviewed against the country scoped defaults. No separately validated sector addition; inherit only defaults applicable to the named country. This is not an exhaustive regulatory inventory.

### telecom | specific | inherits defaults
Use applicable parent notes and these additions only for their named countries and activities.

sector_regulator | scope DE | legal: Germany: section 5 Telekommunikationsgesetz requires notification of covered public networks and publicly available services to Bundesnetzagentur. Number independent interpersonal telecommunications services are excluded from this notification.
Applies only: For the actual provider and service within section 5; other obligations can still apply to excluded services.
Source J:DE-TKG: Meldepflicht <https://www.bundesnetzagentur.de/DE/Fachthemen/Telekommunikation/Unternehmenspflichten/Meldepflicht/start.html>. Checked 2026-11-03. Publication date not shown. German version supplies the exclusion omitted in the shorter English page.

sector_regulator | scope FR | legal: France: Ordonnance n° 2021-650 removed the prior operator declaration under CPCE Article L.33-1. Arcep says operator status still follows the actual activity.
Applies only: For the prior declaration addressed by Arcep; this does not remove numbering, emergency access or other applicable duties.
Source J:FR-TELECOM: Questions fréquentes for communications operators <https://extranet.arcep.fr/communications-electroniques/questions-frequentes>. Checked 2026-11-03. Publication date not shown. Removal of this declaration does not remove other operator obligations.

### cybersecurity | specific | inherits defaults
Use applicable parent notes and these additions only for their named countries and activities.

sector_regulator | scope AT,BE,FR,DE,LU,NL | legal: For an EU buyer, assess Directive (EU) 2022/2555, NIS2, through the named country's implementation and the buyer's entity category. The Commission's transposition tracker is not a substitute for the applicable national instrument.
Applies only: Where NIS2 may cover the entity; do not assume a uniform national filing route or deadline.
Source J:EU-NIS2: NIS2 Directive transposition in EU countries <https://digital-strategy.ec.europa.eu/en/policies/nis-transposition>. Checked 2026-11-03. Publication date not established. Tracker is a state of play, not a final finding of national legal compliance.

proof | scope CH | legal: Switzerland: the Information Security Act and Cybersecurity Ordinance require reporting of qualifying cyberattacks by covered critical infrastructure operators. Show how detection evidence reaches the buyer's reporting owner.
Applies only: Only for covered entities and incidents after checking ordinance exemptions; a security supplier is not automatically the reporting entity.
Source J:CH-CYBER: Legal basis for the reporting obligation <https://www.bacs.admin.ch/en/legal-basis-for-the-reporting-obligation>. Checked 2026-11-03. Publication date not shown. Entity, incident and ordinance exemptions must be checked; not every Swiss company is covered.

### software | inherited | inherits defaults
Reviewed against the country scoped defaults. No separately validated sector addition; inherit only defaults applicable to the named country. This is not an exhaustive regulatory inventory.

### saas | inherited | inherits defaults
Reviewed against the country scoped defaults. No separately validated sector addition; inherit only defaults applicable to the named country. This is not an exhaustive regulatory inventory.

### freight-visibility | inherited | inherits logistics-tech
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### freight-marketplace | inherited | inherits logistics-tech
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### seller-shipping | inherited | inherits logistics-tech
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### last-mile | inherited | inherits logistics-tech
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### warehousing | inherited | inherits logistics-tech
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### transport-management | inherited | inherits logistics-tech
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### payments-banking | specific | inherits fintech
Use applicable parent notes and these additions only for their named countries and activities.

sector_regulator | scope AT,BE,FR,DE,LU,NL | legal: Under Directive (EU) 2015/2366, PSD2, national authorities authorise payment institutions. Use the EBA register to locate the entity and then verify the national authorisation and services.
Applies only: For covered payment or electronic money institutions; the EBA register itself confers no legal rights.
Source J:EU-PSD2: Register of payment and electronic money institutions under PSD2 <https://eba.europa.eu/risk-and-data-analysis/data/registers/payment-institutions-register>. Checked 2026-11-03. Publication date not shown. Central register has no legal significance; national register controls.

sector_regulator | scope DE | legal: Germany: the Zahlungsdiensteaufsichtsgesetz provides BaFin authorisation routes for payment institutions and electronic money institutions. Confirm the actual activity and exclusions.
Applies only: For the activities and institutions within ZAG; do not infer payment institution status from supplying an API.
Source J:DE-PAYMENTS: Payment institutions and electronic money institutions <https://www.bundesbank.de/en/tasks/financial-supervision/individual-aspects/payment-institutions-and-e-money-institutions-622962>. Checked 2026-11-03. Publication date not shown. Exclusions and actual service model must be checked.

### core-banking | specific | inherits fintech
Use applicable parent notes and these additions only for their named countries and activities.

sector_regulator | scope AT | legal: Austria: the ECB lists Finanzmarktaufsicht as the national competent banking supervisor. Confirm the bank's supervisory route before assigning approval evidence.
Applies only: For banking supervision in the Single Supervisory Mechanism; not an investment, insurance or general software regulator mapping.
Source J:EU-BANK-SUPERVISORS: National supervisors <https://www.bankingsupervision.europa.eu/about/organisation/national-supervisors/html/index.en.html>. Checked 2026-11-03. Publication date not shown. Banking supervision only, not a list of every financial sector regulator.

sector_regulator | scope BE | legal: Belgium: the ECB lists National Bank of Belgium as the national competent banking supervisor. Confirm the bank's supervisory route before assigning approval evidence.
Applies only: For banking supervision in the Single Supervisory Mechanism; not an investment, insurance or general software regulator mapping.
Source J:EU-BANK-SUPERVISORS: National supervisors <https://www.bankingsupervision.europa.eu/about/organisation/national-supervisors/html/index.en.html>. Checked 2026-11-03. Publication date not shown. Banking supervision only, not a list of every financial sector regulator.

sector_regulator | scope FR | legal: France: the ECB lists Autorité de contrôle prudentiel et de résolution as the national competent banking supervisor. Confirm the bank's supervisory route before assigning approval evidence.
Applies only: For banking supervision in the Single Supervisory Mechanism; not an investment, insurance or general software regulator mapping.
Source J:EU-BANK-SUPERVISORS: National supervisors <https://www.bankingsupervision.europa.eu/about/organisation/national-supervisors/html/index.en.html>. Checked 2026-11-03. Publication date not shown. Banking supervision only, not a list of every financial sector regulator.

sector_regulator | scope DE | legal: Germany: the ECB lists BaFin as the national competent banking supervisor. Confirm the bank's supervisory route before assigning approval evidence.
Applies only: For banking supervision in the Single Supervisory Mechanism; not an investment, insurance or general software regulator mapping.
Source J:EU-BANK-SUPERVISORS: National supervisors <https://www.bankingsupervision.europa.eu/about/organisation/national-supervisors/html/index.en.html>. Checked 2026-11-03. Publication date not shown. Banking supervision only, not a list of every financial sector regulator.

sector_regulator | scope LU | legal: Luxembourg: the ECB lists Commission de Surveillance du Secteur Financier as the national competent banking supervisor. Confirm the bank's supervisory route before assigning approval evidence.
Applies only: For banking supervision in the Single Supervisory Mechanism; not an investment, insurance or general software regulator mapping.
Source J:EU-BANK-SUPERVISORS: National supervisors <https://www.bankingsupervision.europa.eu/about/organisation/national-supervisors/html/index.en.html>. Checked 2026-11-03. Publication date not shown. Banking supervision only, not a list of every financial sector regulator.

sector_regulator | scope NL | legal: Netherlands: the ECB lists De Nederlandsche Bank as the national competent banking supervisor. Confirm the bank's supervisory route before assigning approval evidence.
Applies only: For banking supervision in the Single Supervisory Mechanism; not an investment, insurance or general software regulator mapping.
Source J:EU-BANK-SUPERVISORS: National supervisors <https://www.bankingsupervision.europa.eu/about/organisation/national-supervisors/html/index.en.html>. Checked 2026-11-03. Publication date not shown. Banking supervision only, not a list of every financial sector regulator.

### lending | specific | inherits fintech
Use applicable parent notes and these additions only for their named countries and activities.

sector_regulator | scope DE | legal: Germany: the Bundesbank explains activity based authorisation under the Kreditwesengesetz. Determine whether the business conducts regulated banking or financial services before assigning a lending permission.
Applies only: For the business's own regulated activity; technology support for a lender does not alone establish authorisation scope.
Source J:DE-FINTECH: FinTech technology enabled financial innovation <https://www.bundesbank.de/en/tasks/financial-supervision/individual-aspects/fintech-622840>. Checked 2026-11-03. Publication date not shown. Fintech is not a separate legal category and not all fintech is regulated.

### wealth-investment | specific | inherits fintech
Use applicable parent notes and these additions only for their named countries and activities.

proof | scope AT,BE,FR,DE,LU,NL | legal: For an EU investment firm, check the national register for the legal entity and authorised investment activities. ESMA's consolidated register points back to national authorities.
Applies only: For regulated investment services; the evidence must match the actual entity and service offered.
Source J:EU-INVEST: Is the firm regulated? <https://www.esma.europa.eu/investor-corner/is-the-firm-regulated>. Checked 2026-11-03. Publication date not shown. Check the actual legal entity and service; database inclusion does not replace licence scope review.

### spend-expense | inherited | inherits fintech
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### insurance | specific | inherits fintech
Use applicable parent notes and these additions only for their named countries and activities.

sector_regulator | scope DE | legal: Germany: an insurtech carrying on insurance business needs the applicable authorisation under the Versicherungsaufsichtsgesetz. BaFin's guidance ties this to the insurance activity.
Applies only: For conducting insurance business, not merely supplying insurance software.
Source J:DE-INSURANCE: Unterliegen Insurtechs einer Aufsichtspflicht? <https://bafin.de/SharedDocs/FAQs/DE/Fintech/Geschaeftsmodelle/Insurtechs/FAQ_Allgemein/4.html>. Checked 2026-11-03. Publication date not shown. German primary text. Does not make every insurance technology vendor an insurer.

sector_regulator | scope FR | legal: France: ACPR's authorisation routes distinguish insurance undertakings from banking institutions. Confirm the prospect's insurance entity and approved activity.
Applies only: For institutions within ACPR's insurance authorisation remit; do not treat a software supplier as an insurer.
Source J:FR-AUTH: Authorising undertakings <https://acpr.banque-france.fr/en/nos-missions/authorising-undertakings>. Checked 2026-11-03. Publication date not shown. Different routes by regulated activity; not all French finance is supervised solely by ACPR.

proof | scope AT,BE,FR,DE,LU,NL | legal: For an EU insurance undertaking, verify authorisation with the relevant national authority. EIOPA states that national registers prevail over conflicting entries in its consolidated register.
Applies only: For insurance undertakings; do not use the same register as proof of an intermediary's permission.
Source J:EU-INSURANCE: Register of Insurance Undertakings <https://register.eiopa.europa.eu/registers/register-of-insurance-undertakings>. Checked 2026-11-03. Publication date not shown. Undertakings and intermediaries differ; national registers prevail.

### customer-service | inherited | inherits saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### crm-marketing | inherited | inherits saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### collaboration | inherited | inherits saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### product-growth | inherited | inherits saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### construction | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### property-management | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### field-services | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### fmcg-retail-execution | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### industry-hr-payroll | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### hotel-lodging | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### retail-restaurant-ops | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### agents-copilots | inherited | inherits ai-native
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### voice-language-models | inherited | inherits ai-native
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### enterprise-search | inherited | inherits ai-native
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### it-services | inherited | inherits ites
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### bpo-cx | inherited | inherits ites
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### digital-engineering | inherited | inherits ites
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### data-services | inherited | inherits ites
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### operators-connectivity | inherited | inherits telecom
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### cpaas-messaging | inherited | inherits telecom
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### telecom-software | inherited | inherits telecom
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### business-voice-ucaas | inherited | inherits telecom
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### developer-platform | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### data-infrastructure | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### observability | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### testing | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### dev-tools | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### cloud-security | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### identity-security | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### email-security | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### awareness-training | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### appsec | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### mobile-appsec | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### soc-services | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### endpoint-network | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### document-ai | inherited | inherits ai-native
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### ai-video | inherited | inherits ai-native
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### engineering-talent | inherited | inherits ites
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### product-management | inherited | inherits saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### digital-adoption | inherited | inherits saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### pentest | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### attack-surface-dast | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### process-orchestration | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### open-source-support | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

### iot-connectivity | inherited | inherits telecom
No validated subtype addition beyond the applicable country notes in the parent and defaults. Do not borrow another country's note.

## North America

This draft covers the United States, Canada and Mexico. It is not one legal market. State, province, territory, buyer type and activity must be established where relevant. No US state rule is presented as national, and no US, Canadian or Mexican rule is borrowed by another country. Draft for owner review.
Countries: US = United States; CA = Canada; MX = Mexico
Clues, only in selling context: {"aliases":["North America"],"countries":[{"code":"US","name":"United States","aliases":["United States","United States of America","USA","U.S."],"cities":["New York","San Francisco","Boston","Chicago","Austin"],"currencies":["USD","US dollar"],"regulators":["Federal Deposit Insurance Corporation","Office of the Comptroller of the Currency","Federal Communications Commission","Securities and Exchange Commission","FinCEN"]},{"code":"CA","name":"Canada","aliases":["Canada"],"cities":["Toronto","Vancouver","Montreal","Ottawa"],"currencies":["CAD","Canadian dollar"],"regulators":["Office of the Superintendent of Financial Institutions","Bank of Canada","Canadian Radio-television and Telecommunications Commission"]},{"code":"MX","name":"Mexico","aliases":["Mexico","México"],"cities":["Mexico City","Ciudad de México","Monterrey","Guadalajara"],"currencies":["MXN","Mexican peso"],"regulators":["Comisión Nacional Bancaria y de Valores","Comisión Nacional de Seguros y Fianzas","Comisión Reguladora de Telecomunicaciones"]}]}

### Defaults

decision_approvers | scope COMMON | question: Which country, state or province and legal entity will buy, and who signs off budget, operational risk and personal data handling?

procurement_payment | scope COMMON | question: What procurement route, invoice currency, tax treatment, acceptance terms and payment schedule has this buyer confirmed?

data_privacy | scope US | operating: United States: the FTC's business guidance recommends documenting the personal data held, restricting access, retaining only what is needed and disposing of it safely. Use that evidence to substantiate security claims.
Applies only: Business security guidance, not a certification or a substitute for state, sector and contractual requirements.
Source J:US-FTC-SECURITY: Start with Security: A Guide for Business <https://www.ftc.gov/business-guidance/resources/start-security-guide-business>. Checked 2026-11-03. Publication date not reliably established. Guidance derived from cases; individual settlement orders do not apply to every business.

data_privacy | scope CA | legal: Canada: under PIPEDA, an organisation remains accountable for personal information sent to a processor and must use contractual or other means to provide comparable protection.
Applies only: For processing within PIPEDA scope. The cited guidance excludes public sector transfers and does not replace provincial rules.
Source J:CA-PIPEDA: Guidelines for processing personal data across borders <https://www.priv.gc.ca/en/privacy-topics/airports-and-borders/gl_dab_090127/>. Checked 2026-11-03. Publication date not reliably established. Does not cover public sector transfers or detailed provincial private sector requirements.

data_privacy | scope CA | legal: Canada: establish the province, sector and data flow before selecting privacy requirements. PIPEDA and provincial laws can govern different parts of the same operation.
Applies only: Private sector commercial processing; do not present one province's law as the rule for all of Canada.
Source J:CA-PROVINCES: Provincial laws that may apply instead of PIPEDA <https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/r_o_p/prov-pipeda>. Checked 2026-11-03. Publication date not reliably established. Sector, province and data flow determine applicable law.

data_privacy | scope MX | legal: Mexico: use the Ley Federal de Protección de Datos Personales en Posesión de los Particulares to establish the responsible party and processor roles. The law designates Secretaría Anticorrupción y Buen Gobierno as the Secretaría.
Applies only: For private sector processing within the law, after checking its exclusions; public sector processing has a different instrument.
Source J:MX-PRIVACY: Decree issuing the private sector personal data protection law <https://sidof.segob.gob.mx/notas/docFuente/5752569>. Checked 2026-11-03. The decree contains multiple laws. Notes refer only to the private sector law in Artículo Tercero; exceptions and subsequent amendments require care.

buyer_language | scope COMMON | question: Which language does the buying team require for the contract, implementation, evidence and support?

proof | scope COMMON | question: Which local workflow and buyer approved acceptance test will show that the proposed outcome is achievable?

objections | scope COMMON | question: Which unresolved approval requirement is most likely to block the purchase, and who can validate the evidence?

sales_motion | scope COMMON | question: Who owns the pilot, its success criteria and the decision to fund the next stage in each market?

### logistics-tech | specific | inherits defaults
Applicable parent notes remain. Add only the following country and activity scoped evidence.

sector_regulator | scope MX | legal: Mexico: NOM-087-SCT-2-2017 addresses driving and break times for drivers in federal motor transport services. Confirm that the operator's service is within this scope.
Applies only: For covered federal motor transport services; do not import US or Canadian hours rules.
Source J:MX-ROAD: NOM-087-SCT-2-2017 <https://platiica.economia.gob.mx/normalizacion/nom-087-sct-2-2017/>. Checked 2026-11-03. Catalogue supports identity and scope, not detailed timing claims. Verify the operator's covered activity.

proof | scope US | legal: United States: for operations covered by 49 CFR Part 395, demonstrate the driver's duty record and electronic logging workflow, including the applicable exceptions.
Applies only: For covered US motor carrier operations. Software supply alone does not make the supplier a motor carrier.
Source J:US-ELD: General Information about the ELD Rule <https://www.fmcsa.dot.gov/hours-service/elds/general-information-about-eld-rule>. Checked 2026-11-03. Publication date not shown. Applies to covered US operations, including certain foreign domiciled drivers, not all fleet software.

proof | scope CA | legal: Canada: for a covered federal motor carrier operation, verify the electronic logging device against the Commercial Vehicle Drivers Hours of Service Regulations and Transport Canada's certification requirement.
Applies only: For federally regulated operations after checking exemptions; US compliance alone does not establish Canadian compliance.
Source J:CA-ELD: Electronic logging devices for commercial drivers and motor carriers <https://tc.canada.ca/en/road-transportation/electronic-logging-devices/electronic-logging-devices-commercial-drivers-motor-carriers>. Checked 2026-11-03. Publication date not shown. Federal scope and listed exemptions matter; US compliance alone is not sufficient.

### fintech | specific | inherits defaults
Applicable parent notes remain. Add only the following country and activity scoped evidence.

decision_approvers | scope CA | legal: Canada: OSFI Guideline B-10 leaves accountability with the federally regulated financial institution. Identify its third party risk owner and match evidence to the arrangement's risk and criticality.
Applies only: Only for federally regulated financial institutions and covered branches, not every provincial financial business.
Source J:CA-OSFI-B10: Third Party Risk Management Guideline B-10 <https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/third-party-risk-management-guideline>. Checked 2026-11-03. Guidance scope is federally regulated institutions and relevant branches, not every Canadian fintech or provincial insurer.

sector_regulator | scope MX | legal: Mexico: the Ley para Regular las Instituciones de Tecnología Financiera distinguishes collective financing institutions and electronic payment fund institutions. Confirm the actual activity before selecting the CNBV authorisation route.
Applies only: For the designated financial institutions and activities covered by the law; a fintech label does not put every software supplier in scope.
Source J:MX-FINTECH: Instituciones de Tecnología Financiera <https://www.gob.mx/cnbv/acciones-y-programas/instituciones-de-tecnologia-financiera>. Checked 2026-11-03. Publication date not reliably captured. Scope is designated financial institutions, not all businesses described as fintech.

procurement_payment | scope US | legal: United States: align a bank buyer's evidence review with the OCC, Federal Reserve and FDIC Interagency Guidance on Third Party Relationships. Prepare for due diligence, contract review, monitoring and exit planning.
Applies only: For banking organisations supervised by the issuing agencies; expectations depend on the arrangement's risk and complexity.
Source J:US-BANK-THIRDPARTY: Interagency Guidance on Third Party Relationships: Risk Management <https://www.fdic.gov/news/financial-institution-letters/2023/fil23029.html>. Checked 2026-11-03. Supervisory guidance, not a new licence or a universal checklist for every nonbank.

### vertical-saas | inherited | inherits defaults
No validated sector addition beyond the country scoped defaults. Inherit only notes for the named country; this is not a complete regulatory inventory.

### ai-native | specific | inherits defaults
Applicable parent notes remain. Add only the following country and activity scoped evidence.

proof | scope US | operating: United States: if the buyer uses the NIST AI Risk Management Framework, organise evidence around the risks of the actual use case. NIST describes the framework as voluntary.
Applies only: Use only as an agreed assurance framework; do not represent it as a general legal approval or claim it is uniquely applicable to the US.
Source J:US-AI-RMF: AI Risk Management Framework <https://www.nist.gov/itl/ai-risk-management-framework>. Checked 2026-11-03. Webpage publication date not established. Framework release date 2023-01-26. Not a general legal mandate.

### ites | inherited | inherits defaults
No validated sector addition beyond the country scoped defaults. Inherit only notes for the named country; this is not a complete regulatory inventory.

### telecom | specific | inherits defaults
Applicable parent notes remain. Add only the following country and activity scoped evidence.

sector_regulator | scope CA | legal: Canada: CRTC registration and the relevant provider obligations depend on the telecommunications service supplied. The CRTC lists specific reseller exemptions; an exemption from registration does not remove all consumer duties.
Applies only: For Canadian telecommunications provision; establish provider type, services and exemptions before assigning obligations.
Source J:CA-TELECOM: Responsibilities and Regulatory Obligations for Non Facilities Based Providers <https://crtc.gc.ca/eng/comm/telecom/respnon.htm>. Checked 2026-11-03. Publication date not shown. Registration exemptions do not remove all consumer protections.

sector_regulator | scope US | legal: United States: a covered interconnected voice service must be assessed against the FCC E911 requirements in 47 CFR 9.11. Establish the service classification and geographic scope first.
Applies only: Only for interconnected VoIP services and calls within the rule's scope; do not extend this to all communications software.
Source J:US-E911: 47 CFR 9.11 E911 Service <https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-9/subpart-D/section-9.11>. Checked 2026-11-03. Publication date omitted for continuously updated code; latest amendment shown 2026-01-14. Geographic service conditions and fixed versus nonfixed service matter.

proof | scope MX | legal: Mexico: verify the operator's service, territory and authorisation validity in the Comisión Reguladora de Telecomunicaciones public concessions register.
Applies only: For a relevant concession, permit or authorisation; registry verification does not establish that every telecom software vendor needs one.
Source J:MX-TELECOM: Registro Público de Concesiones <https://rpc.crt.gob.mx/vrpc>. Checked 2026-11-03. Publication date not shown. Registry supports verification, not a general conclusion that every telecom software supplier needs a concession.

### cybersecurity | specific | inherits defaults
Applicable parent notes remain. Add only the following country and activity scoped evidence.

proof | scope US | operating: United States: ask whether the buyer's contract requires the NIST Cybersecurity Framework. NIST says most organisations use it voluntarily; the framework is not itself a regulatory certification.
Applies only: A government or contractual requirement needs its own scope check; do not infer a universal mandate.
Source J:US-CSF: Frequently Asked Questions about the Cybersecurity Framework <https://www.nist.gov/cyberframework/faqs>. Checked 2026-11-03. Publication date not shown. NIST is not a regulatory agency; individual obligations need separate evidence.

proof | scope CA | operating: Canada: the Canadian Centre for Cyber Security's baseline guidance recommends a written incident plan with named responsibilities. Show the buyer how the proposed service fits its response process.
Applies only: Recommended baseline guidance for small and medium organisations; confirm suitability for the buyer's risk rather than asserting certification.
Source J:CA-CYBER: Baseline cyber security controls for small and medium organizations <https://www.cyber.gc.ca/en/guidance/baseline-cyber-security-controls-small-and-medium-organizations>. Checked 2026-11-03. Publication date not reliably established. Voluntary guidance targeted at smaller organisations, not a universal certification requirement.

### software | inherited | inherits defaults
No validated sector addition beyond the country scoped defaults. Inherit only notes for the named country; this is not a complete regulatory inventory.

### saas | inherited | inherits defaults
No validated sector addition beyond the country scoped defaults. Inherit only notes for the named country; this is not a complete regulatory inventory.

### freight-visibility | inherited | inherits logistics-tech
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### freight-marketplace | inherited | inherits logistics-tech
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### seller-shipping | inherited | inherits logistics-tech
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### last-mile | inherited | inherits logistics-tech
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### warehousing | inherited | inherits logistics-tech
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### transport-management | inherited | inherits logistics-tech
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### payments-banking | specific | inherits fintech
Applicable parent notes remain. Add only the following country and activity scoped evidence.

sector_regulator | scope US | legal: United States: determine whether the actual funds activity makes the entity a money services business under 31 CFR Chapter X. FinCEN registration has exceptions, including a person acting solely as another MSB's agent.
Applies only: For federal MSB registration scope; this does not settle state licensing, bank charter or other obligations.
Source J:US-FINCEN: Money Services Business Registration <https://www.fincen.gov/resources/money-services-business-msb-registration>. Checked 2026-11-03. Publication date not shown. Federal registration is not a determination of state licensing or banking authority.

sector_regulator | scope MX | legal: Mexico: an institution issuing, administering, redeeming or transmitting electronic payment funds can fall within the CNBV electronic payment fund institution category under the Ley para Regular las Instituciones de Tecnología Financiera.
Applies only: Only where the actual activity matches the statutory category; an API or accounting feature alone is insufficient.
Source J:MX-FINTECH: Instituciones de Tecnología Financiera <https://www.gob.mx/cnbv/acciones-y-programas/instituciones-de-tecnologia-financiera>. Checked 2026-11-03. Publication date not reliably captured. Scope is designated financial institutions, not all businesses described as fintech.

proof | scope CA | legal: Canada: a payment service provider within the Retail Payment Activities Act needs the applicable operational risk, incident response and end user funds safeguards. Show how the buyer's framework handles the proposed service.
Applies only: For payment activities and providers within RPAA scope; determine whether funds are held and check exclusions.
Source J:CA-RPAA: Retail payments supervisory framework <https://www.bankofcanada.ca/regulatory-oversight/retail-payments/supervisory-framework/>. Checked 2026-11-03. Publication date not shown. Apply only to payment service providers and activities in scope; check exclusions and funds handling.

### core-banking | specific | inherits fintech
Applicable parent notes remain. Add only the following country and activity scoped evidence.

proof | scope US | legal: United States: a bank's use of a third party does not remove its responsibility for safe operations and applicable law. Provide control and monitoring evidence for the bank's chosen supervisory review.
Applies only: For a supervised bank relationship; a core banking platform supplier does not inherit the bank's charter.
Source J:US-BANK-THIRDPARTY: Interagency Guidance on Third Party Relationships: Risk Management <https://www.fdic.gov/news/financial-institution-letters/2023/fil23029.html>. Checked 2026-11-03. Supervisory guidance, not a new licence or a universal checklist for every nonbank.

proof | scope CA | legal: Canada: OSFI B-10 applies proportionate oversight to a federally regulated institution's third party arrangement. Agree the criticality and continuity evidence with the institution.
Applies only: For institutions within B-10 scope; do not assume provincial institutions have the same supervisory route.
Source J:CA-OSFI-B10: Third Party Risk Management Guideline B-10 <https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/third-party-risk-management-guideline>. Checked 2026-11-03. Guidance scope is federally regulated institutions and relevant branches, not every Canadian fintech or provincial insurer.

### lending | specific | inherits fintech
Applicable parent notes remain. Add only the following country and activity scoped evidence.

proof | scope US | legal: United States: under ECOA Regulation B, 12 CFR 1002.9, required adverse action reasons must identify the principal factors actually used. Demonstrate the explanation workflow for the creditor's applicable notice route.
Applies only: For covered credit decisions and notices; check business credit, incomplete application and other exceptions rather than applying one notice process to every loan.
Source J:US-REG-B: 12 CFR 1002.9 Notifications <https://www.consumerfinance.gov/rules-policy/regulations/1002/9/>. Checked 2026-11-03. No standalone publication date shown. Direct rule used instead of relying on an older circular. Business credit and other notification exceptions must be checked.

### wealth-investment | specific | inherits fintech
Applicable parent notes remain. Add only the following country and activity scoped evidence.

sector_regulator | scope US | legal: United States: an investment adviser may be registered with the SEC or one or more state securities authorities. Verify the entity's actual registration and applicable exceptions before assigning an approval route.
Applies only: Investment adviser registration only; not the registration regime for every broker, fund or software supplier.
Source J:US-ADVISERS: Investment Adviser Registration <https://www.investor.gov/introduction-investing/getting-started/working-investment-professional/investment-advisers-0>. Checked 2026-11-03. Publication date not shown. Investment advisers differ from brokers and other financial intermediaries.

sector_regulator | scope CA | legal: Canada: National Instrument 31-103 and related rules govern dealer and adviser registration through provincial and territorial securities authorities. Verify the category, permitted activity and exemptions.
Applies only: For covered securities businesses; the national search does not create a federal securities licence.
Source J:CA-SECURITIES: Registration Information <https://www.securities-administrators.ca/industry-resources/registration-information/>. Checked 2026-11-03. Publication date not shown. Check exemptions, registration category and principal regulator; not a federal securities licence.

### spend-expense | specific | inherits fintech
Applicable parent notes remain. Add only the following country and activity scoped evidence.

sector_regulator | scope CA | legal: Canada: assess any actual retail payment function in an expense product against the Retail Payment Activities Act before promising a payment service.
Applies only: Only if the service performs covered payment functions; expense record keeping alone does not establish RPAA scope.
Source J:CA-RPAA: Retail payments supervisory framework <https://www.bankofcanada.ca/regulatory-oversight/retail-payments/supervisory-framework/>. Checked 2026-11-03. Publication date not shown. Apply only to payment service providers and activities in scope; check exclusions and funds handling.

### insurance | specific | inherits fintech
Applicable parent notes remain. Add only the following country and activity scoped evidence.

sector_regulator | scope US | legal: United States: insurance regulation is primarily state based. NAIC supports state regulators but does not issue licences, and a model law is not automatically law in any state.
Applies only: Identify the relevant state and adopted instrument before attaching a specific insurance or cyber obligation.
Source J:US-INSURANCE: Understanding the NAIC: Governance and Accountability <https://content.naic.org/about/understanding-naic-governance-accountability>. Checked 2026-11-03. Publication date not shown. NAIC is a regulatory support body, not a licensing regulator. Check state enactments separately.

sector_regulator | scope MX | legal: Mexico: establishing an insurance institution requires the corresponding CNSF authorisation. Keep this approval route separate from CNBV fintech authorisation.
Applies only: For establishing an insurance institution; not every insurance intermediary or technology supplier.
Source J:MX-INSURANCE: Autorización para constituir, organizar y funcionar como Institución de Seguros <https://www.gob.mx/cnsf/acciones-y-programas/autorizacion-para-constituir-organizar-y-funcionar-como-institucion-de-seguros>. Checked 2026-11-03. Applies to establishing an insurance institution, not every intermediary or software supplier.

buyer_language | scope MX | legal: Mexico: the CNSF insurance institution application requires the specified documents in Spanish. Prepare the approval evidence in the required language.
Applies only: Only for that authorisation application; this does not establish the language preference of every private buyer.
Source J:MX-INSURANCE: Autorización para constituir, organizar y funcionar como Institución de Seguros <https://www.gob.mx/cnsf/acciones-y-programas/autorizacion-para-constituir-organizar-y-funcionar-como-institucion-de-seguros>. Checked 2026-11-03. Applies to establishing an insurance institution, not every intermediary or software supplier.

### customer-service | inherited | inherits saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### crm-marketing | inherited | inherits saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### collaboration | inherited | inherits saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### product-growth | inherited | inherits saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### construction | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### property-management | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### field-services | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### fmcg-retail-execution | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### industry-hr-payroll | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### hotel-lodging | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### retail-restaurant-ops | inherited | inherits vertical-saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### agents-copilots | inherited | inherits ai-native
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### voice-language-models | inherited | inherits ai-native
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### enterprise-search | inherited | inherits ai-native
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### it-services | inherited | inherits ites
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### bpo-cx | inherited | inherits ites
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### digital-engineering | inherited | inherits ites
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### data-services | inherited | inherits ites
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### operators-connectivity | inherited | inherits telecom
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### cpaas-messaging | inherited | inherits telecom
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### telecom-software | inherited | inherits telecom
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### business-voice-ucaas | specific | inherits telecom
Applicable parent notes remain. Add only the following country and activity scoped evidence.

proof | scope US | legal: United States: for a covered interconnected VoIP service, test emergency routing, location handling and the required subscriber notice of service limitations under 47 CFR 9.11.
Applies only: Match fixed or nonfixed service requirements and the rule's geographic conditions.
Source J:US-E911: 47 CFR 9.11 E911 Service <https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-9/subpart-D/section-9.11>. Checked 2026-11-03. Publication date omitted for continuously updated code; latest amendment shown 2026-01-14. Geographic service conditions and fixed versus nonfixed service matter.

### developer-platform | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### data-infrastructure | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### observability | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### testing | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### dev-tools | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### cloud-security | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### identity-security | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### email-security | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### awareness-training | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### appsec | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### mobile-appsec | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### soc-services | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### endpoint-network | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### document-ai | inherited | inherits ai-native
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### ai-video | inherited | inherits ai-native
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### engineering-talent | inherited | inherits ites
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### product-management | inherited | inherits saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### digital-adoption | inherited | inherits saas
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### pentest | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### attack-surface-dast | inherited | inherits cybersecurity
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### process-orchestration | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### open-source-support | inherited | inherits software
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.

### iot-connectivity | inherited | inherits telecom
No validated subtype addition beyond the applicable country notes in the parent and defaults. State or provincial rules must not be inferred.
