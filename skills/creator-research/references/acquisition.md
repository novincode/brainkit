# Acquisition and capability limits

Start with manual source selection. APIs help scale retrieval after the annotation workflow works.

| Need | Route | Limitation |
|---|---|---|
| Public video metadata | YouTube Data API or inspected public page | Metadata does not contain a full story or retention curve |
| Captions for owned/editable videos | Authorized captions workflow | Official caption download requires permission to edit the video |
| Other creators' scripts | Published transcripts, supplied text, or appropriate permitted access | An API key is not universal transcript access |
| Visual decisions | Accessible video inspection or supplied media; frames for bounded visual questions | Sparse frames miss cuts, transitions, and delivery |
| Delivery | Listen to actual audio | Transcript punctuation cannot prove performance |
| Retention and source mix | Creator-authorized analytics/export | Normally unavailable for arbitrary other channels |

For supplied media: align a transcript to time, inspect the opening and turning points, then inspect continuous sections for timing claims. Capture actual inspected intervals. ASR needs correction for names, negation, numbers, and overlapping speech.

For scraping or third-party transcript tools: assess the specific site's current access rules, reliability, rights, and costs first. Never bypass access controls. Prefer a small manual pilot to a broad scraper. Revalidate provider capabilities and quotas at implementation time.

Official references: https://developers.google.com/youtube/v3/docs/captions/download and https://support.google.com/youtube/answer/9314415. Retrieval baseline: 2026-10-19. Refresh before implementing an integration.
